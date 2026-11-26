#!/usr/bin/env python3
"""Verify the Conjectura Lean library and write a verification receipt.

The script runs, in order, and fails if any step is missing or unsuccessful:

1. toolchain   the installed Lean matches ``formalization/lean-toolchain`` and
               the Mathlib revision in the manifest matches the pin in the lakefile;
2. build       ``lake build <root module>`` succeeds;
3. sources     no forbidden construct (``sorry``, ``admit``, ``axiom``,
               ``native_decide``, ``unsafe``, ``implemented_by``, ``extern``,
               ``debug.skipKernelTC``) occurs in project sources outside comments;
4. axioms      every project-owned declaration depends, transitively, only on
               the permitted axioms, and no project declaration is an axiom, is
               unsafe, partial or opaque;
5. registry    every theorem registered in ``formalization/registry.json``
               exists, is a theorem, has the reviewed statement fingerprint, and
               has a non-vacuity witness (or a stated reason why none is needed);
6. replay      ``leanchecker`` re-checks the compiled project modules with the
               Lean kernel.

Policy and rationale: ``docs/verification-policy.md``.

Usage::

    python scripts/verify_lean.py                    # full run, writes a receipt
    python scripts/verify_lean.py --no-receipt       # full run, no receipt
    python scripts/verify_lean.py --show-fingerprints  # print current fingerprints
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAKE_DIR = ROOT / "formalization"
REGISTRY = LAKE_DIR / "registry.json"
RECEIPTS = ROOT / "verification" / "receipts"
AUDIT_TEMPLATE = ROOT / "scripts" / "lean_audit_template.lean"

DEFAULT_MODULE = "Conjectura"

# The standard axioms of Lean 4 used throughout Mathlib. Nothing else is allowed.
ALLOWED_AXIOMS = frozenset({"propext", "Classical.choice", "Quot.sound"})

# Constructs that must not appear in the verified library (checked on sources
# with comments and string literals removed). The axiom audit is the
# authoritative check; this scan gives early, readable diagnostics and catches
# options that do not show up as axioms.
FORBIDDEN_SOURCE_PATTERNS: dict[str, str] = {
    "sorry": r"\bsorry\b",
    "admit": r"\badmit\b",
    "native_decide": r"\bnative_decide\b",
    "axiom declaration": r"(?m)^\s*(?:(?:private|protected|noncomputable|public)\s+)*axiom\b",
    "unsafe": r"\bunsafe\b",
    "implemented_by": r"\bimplemented_by\b",
    "extern": r"@\[\s*extern\b",
    "debug.skipKernelTC": r"debug\.skipKernelTC",
}

PASSED, FAILED, NOT_RUN = "passed", "failed", "not-run"


@dataclasses.dataclass
class Check:
    name: str
    status: str
    details: list[str] = dataclasses.field(default_factory=list)

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Command:
    argv: list[str]
    returncode: int | None
    seconds: float
    output_tail: str

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Report:
    module: str
    checks: list[Check] = dataclasses.field(default_factory=list)
    commands: list[Command] = dataclasses.field(default_factory=list)
    declarations: list[dict] = dataclasses.field(default_factory=list)
    registry: list[dict] = dataclasses.field(default_factory=list)
    toolchain: dict = dataclasses.field(default_factory=dict)

    @property
    def verdict(self) -> str:
        """``passed`` only if every check ran and passed."""
        if self.checks and all(check.status == PASSED for check in self.checks):
            return PASSED
        return FAILED

    def check(self, name: str) -> Check:
        for check in self.checks:
            if check.name == name:
                return check
        raise KeyError(name)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------


def find_tool(name: str) -> str | None:
    """Locate a Lean tool on PATH or in the default elan directory."""
    found = shutil.which(name)
    if found:
        return found
    candidate = Path.home() / ".elan" / "bin" / (name + (".exe" if os.name == "nt" else ""))
    return str(candidate) if candidate.is_file() else None


def run(argv: list[str], report: Report, timeout: int = 3600) -> subprocess.CompletedProcess | None:
    """Run a command inside the Lake project and record it in the report."""
    started = time.monotonic()
    try:
        completed = subprocess.run(
            argv, cwd=LAKE_DIR, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        report.commands.append(Command(portable(argv), None, round(time.monotonic() - started, 1), portable_text(repr(error))))
        return None
    combined = (completed.stdout or "") + (completed.stderr or "")
    # Keep the tail without the (long) JSON audit payload.
    tail = "\n".join(line for line in combined.splitlines() if not line.startswith("[{"))[-2000:]
    report.commands.append(Command(portable(argv), completed.returncode, round(time.monotonic() - started, 1), portable_text(tail)))
    return completed


def portable(argv: list[str]) -> list[str]:
    """Command line as recorded in receipts: no machine-specific absolute paths."""
    recorded = []
    for argument in argv:
        path = Path(argument)
        if path.is_absolute():
            try:
                argument = path.resolve().relative_to(ROOT).as_posix()
            except ValueError:
                argument = path.stem if path.suffix.lower() == ".exe" else path.name
        recorded.append(argument)
    return recorded


def portable_text(text: str) -> str:
    """Remove the repository location and the home directory from captured output."""
    home = Path.home()
    for location, replacement in ((str(ROOT), "<repo>"), (ROOT.as_posix(), "<repo>"), (str(home), "~"), (home.as_posix(), "~")):
        text = text.replace(location, replacement)
    return text


def sha256_text_file(path: Path) -> str:
    """SHA-256 of a text file with line endings normalised to LF.

    Normalisation makes the hash independent of the checkout platform.
    """
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def strip_comments_and_strings(text: str) -> str:
    """Blank out Lean comments (nested ``/- -/``, ``--``) and string literals."""
    out: list[str] = []
    i, depth, n = 0, 0, len(text)
    while i < n:
        two = text[i : i + 2]
        if depth:
            if two == "/-":
                depth += 1
                i += 2
            elif two == "-/":
                depth -= 1
                i += 2
            else:
                out.append("\n" if text[i] == "\n" else " ")
                i += 1
        elif two == "/-":
            depth = 1
            i += 2
        elif two == "--":
            while i < n and text[i] != "\n":
                i += 1
        elif text[i] == '"':
            i += 1
            while i < n and text[i] != '"':
                i += 2 if text[i] == "\\" else 1
            i += 1
            out.append('""')
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def scan_source(text: str) -> list[str]:
    """Return the names of forbidden constructs present in a Lean source text."""
    stripped = strip_comments_and_strings(text)
    return [name for name, pattern in FORBIDDEN_SOURCE_PATTERNS.items() if re.search(pattern, stripped)]


def module_sources(module: str) -> list[Path]:
    """Source files of a root module: ``X.lean`` and everything under ``X/``."""
    relative = Path(*module.split("."))
    files: list[Path] = []
    single = LAKE_DIR / relative.with_suffix(".lean")
    if single.is_file():
        files.append(single)
    directory = LAKE_DIR / relative
    if directory.is_dir():
        files.extend(sorted(directory.rglob("*.lean")))
    return files


def fingerprint(declaration: dict) -> str:
    """Fingerprint of a theorem statement: pretty-printed type plus structural hash."""
    payload = f"{declaration['statement']}\n{declaration['type_hash']}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def is_auxiliary(name: str) -> bool:
    """Compiler-generated helper declarations (kept in the audit, not listed by name)."""
    return "._" in name or name.startswith("_")


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------


def check_toolchain(report: Report, lake: str) -> None:
    check = Check("toolchain", PASSED)
    pinned = (LAKE_DIR / "lean-toolchain").read_text(encoding="utf-8").strip()
    version = pinned.rsplit(":v", 1)[-1]
    completed = run([lake, "env", "lean", "--version"], report, timeout=600)
    actual = (completed.stdout.strip() if completed else "") or "unavailable"
    if not completed or completed.returncode != 0 or f"version {version}," not in actual:
        check.status = FAILED
        check.details.append(f"pinned {pinned!r} but `lean --version` reports {actual!r}")

    lakefile = (LAKE_DIR / "lakefile.toml").read_text(encoding="utf-8")
    pin = re.search(r'name\s*=\s*"mathlib".*?rev\s*=\s*"([^"]+)"', lakefile, flags=re.S)
    manifest = json.loads((LAKE_DIR / "lake-manifest.json").read_text(encoding="utf-8"))
    mathlib = next((package for package in manifest["packages"] if package["name"] == "mathlib"), None)
    if not pin or not mathlib:
        check.status = FAILED
        check.details.append("could not read the Mathlib pin from lakefile.toml or lake-manifest.json")
    elif mathlib.get("inputRev") != pin.group(1):
        check.status = FAILED
        check.details.append(f"lakefile pins Mathlib {pin.group(1)!r} but the manifest was resolved from {mathlib.get('inputRev')!r}")

    report.toolchain = {
        "lean_toolchain_file": pinned,
        "lean_version": actual,
        "mathlib_input_rev": mathlib.get("inputRev") if mathlib else None,
        "mathlib_commit": mathlib.get("rev") if mathlib else None,
    }
    report.checks.append(check)


def check_build(report: Report, lake: str, module: str) -> bool:
    completed = run([lake, "build", module], report)
    ok = completed is not None and completed.returncode == 0
    details = [] if ok else ["`lake build` failed; see the recorded command output"]
    report.checks.append(Check("build", PASSED if ok else FAILED, details))
    return ok


def check_sources(report: Report, module: str) -> None:
    check = Check("sources", PASSED)
    files = module_sources(module)
    if not files:
        check.status = FAILED
        check.details.append(f"no source files found for module {module}")
    for path in files:
        for construct in scan_source(path.read_text(encoding="utf-8")):
            check.status = FAILED
            check.details.append(f"{path.relative_to(ROOT).as_posix()}: forbidden construct `{construct}`")
    report.checks.append(check)


def run_audit(report: Report, lake: str, module: str, prefix: str) -> list[dict] | None:
    """Elaborate the audit file and return one record per project declaration."""
    audit_dir = LAKE_DIR / ".lake" / "conjectura-audit"
    audit_dir.mkdir(parents=True, exist_ok=True)
    audit_file = audit_dir / f"Audit_{module.replace('.', '_')}.lean"
    template = AUDIT_TEMPLATE.read_text(encoding="utf-8")
    audit_file.write_text(template.replace("__MODULE__", module).replace("__PREFIX__", prefix), encoding="utf-8", newline="\n")
    completed = run([lake, "env", "lean", str(audit_file)], report)
    if completed is None or completed.returncode != 0:
        return None
    lines = completed.stdout.splitlines()
    try:
        payload = lines[lines.index("CONJECTURA_AUDIT_BEGIN") + 1]
        if lines[lines.index("CONJECTURA_AUDIT_BEGIN") + 2] != "CONJECTURA_AUDIT_END":
            return None
        return json.loads(payload)
    except (ValueError, IndexError, json.JSONDecodeError):
        return None


def check_axioms(report: Report, declarations: list[dict] | None) -> None:
    check = Check("axioms", PASSED)
    if declarations is None:
        check.status = FAILED
        check.details.append("the audit did not produce output; nothing was audited")
    elif not declarations:
        check.status = FAILED
        check.details.append("the audit found no project-owned declarations; nothing was audited")
    else:
        for declaration in declarations:
            name = declaration["name"]
            foreign = sorted(set(declaration["axioms"]) - ALLOWED_AXIOMS)
            if declaration["kind"] == "axiom":
                check.details.append(f"{name}: is a project-declared axiom")
            elif foreign:
                check.details.append(f"{name}: depends on non-permitted axiom(s) {foreign}")
            if declaration["kind"] == "opaque":
                check.details.append(f"{name}: is opaque")
            if declaration["unsafe"]:
                check.details.append(f"{name}: is unsafe")
            if declaration["partial"]:
                check.details.append(f"{name}: is partial")
        if check.details:
            check.status = FAILED
    report.checks.append(check)


def check_registry(report: Report, declarations: list[dict] | None, registry: dict, catalogue_ids: set[str]) -> None:
    check = Check("registry", PASSED)
    by_name = {declaration["name"]: declaration for declaration in (declarations or [])}

    def good_theorem(name: str) -> str | None:
        declaration = by_name.get(name)
        if declaration is None:
            return "not found among project declarations"
        if declaration["kind"] != "theorem":
            return f"is a {declaration['kind']}, not a theorem"
        if set(declaration["axioms"]) - ALLOWED_AXIOMS:
            return "depends on non-permitted axioms"
        return None

    entries = registry.get("theorems", [])
    if not entries:
        check.status = FAILED
        check.details.append("the registry lists no theorems; there is nothing to certify")
    for entry in entries:
        name = entry.get("name", "<unnamed>")
        problem = good_theorem(name)
        record = {"name": name, "kind": entry.get("kind"), "catalogue_id": entry.get("catalogue_id")}
        if problem:
            check.details.append(f"{name}: {problem}")
            report.registry.append(record)
            continue
        declaration = by_name[name]
        record |= {
            "module": declaration["module"],
            "statement": declaration["statement"],
            "axioms": sorted(declaration["axioms"]),
            "statement_fingerprint": fingerprint(declaration),
        }
        report.registry.append(record)

        if entry.get("statement_fingerprint") != record["statement_fingerprint"]:
            check.details.append(
                f"{name}: statement fingerprint differs from the reviewed one; the statement changed "
                "or was never reviewed (re-review, then update formalization/registry.json)"
            )

        kind = entry.get("kind")
        in_calibration = declaration["module"].startswith("Conjectura.Calibration")
        if kind == "calibration":
            if not in_calibration:
                check.details.append(f"{name}: registered as calibration but defined in {declaration['module']}")
        elif kind == "research":
            if in_calibration:
                check.details.append(f"{name}: registered as research but defined in a calibration module")
            if entry.get("catalogue_id") not in catalogue_ids:
                check.details.append(f"{name}: catalogue_id {entry.get('catalogue_id')!r} is neither a problem of research/catalogue.json nor a contribution of research/discoveries.json")
            if not entry.get("source_statement"):
                check.details.append(f"{name}: research theorems must cite the source statement they formalize")
        else:
            check.details.append(f"{name}: kind must be 'calibration' or 'research', got {kind!r}")

        nonvacuity = entry.get("nonvacuity") or {}
        if "witness" in nonvacuity:
            witness_problem = good_theorem(nonvacuity["witness"])
            if witness_problem:
                check.details.append(f"{name}: non-vacuity witness {nonvacuity['witness']}: {witness_problem}")
        elif not str(nonvacuity.get("not_needed", "")).strip():
            check.details.append(f"{name}: no non-vacuity witness and no stated reason why none is needed")

    if check.details:
        check.status = FAILED
    report.checks.append(check)


def check_replay(report: Report, lake: str, declarations: list[dict] | None) -> None:
    check = Check("replay", PASSED)
    if not find_tool("leanchecker"):
        report.checks.append(Check("replay", NOT_RUN, ["`leanchecker` is not available in this toolchain"]))
        return
    modules = sorted({declaration["module"] for declaration in (declarations or [])})
    if not modules:
        report.checks.append(Check("replay", NOT_RUN, ["no project modules to replay"]))
        return
    # One invocation per module that owns declarations. (Observed with Lean
    # 4.36.0 on Windows: leanchecker segfaults when asked to replay several
    # modules in one invocation, or the root module, which expands to several;
    # single modules replay normally.)
    for module in modules:
        completed = run([lake, "env", "leanchecker", module], report)
        if completed is None or completed.returncode != 0:
            check.status = FAILED
            code = "no exit status" if completed is None else f"exit status {completed.returncode}"
            check.details.append(f"leanchecker rejected or failed on {module} ({code})")
        else:
            check.details.append(f"replayed {module}")
    report.checks.append(check)


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------


def verify(
    module: str = DEFAULT_MODULE,
    prefix: str | None = None,
    registry: dict | None = None,
    replay: bool = True,
) -> Report:
    """Run every check for ``module`` and return the report.

    ``registry`` defaults to ``formalization/registry.json``. ``replay=False``
    records the replay check as not run, which makes the verdict ``failed``;
    it exists only so that tests of the other checks stay fast.
    """
    report = Report(module=module)
    prefix = prefix or module.split(".")[0]
    lake = find_tool("lake")
    if lake is None:
        report.checks.append(Check("toolchain", NOT_RUN, ["`lake` not found on PATH or in ~/.elan/bin"]))
        return report

    check_toolchain(report, lake)
    built = check_build(report, lake, module)
    check_sources(report, module)
    declarations = run_audit(report, lake, module, prefix) if built else None
    report.declarations = declarations or []
    check_axioms(report, declarations)

    if registry is None:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    # A research theorem backs a catalogued problem (CJ-XXXX) or a registered contribution (MD-XXXX).
    catalogue = json.loads((ROOT / "research" / "catalogue.json").read_text(encoding="utf-8"))
    discoveries = json.loads((ROOT / "research" / "discoveries.json").read_text(encoding="utf-8"))
    record_ids = {problem["id"] for problem in catalogue["problems"]} | {record["id"] for record in discoveries["discoveries"]}
    check_registry(report, declarations, registry, record_ids)

    if replay and built:
        check_replay(report, lake, declarations)
    else:
        reason = "skipped on request" if built else "the build failed"
        report.checks.append(Check("replay", NOT_RUN, [reason]))
    return report


def git(*args: str) -> str:
    completed = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    return completed.stdout.strip() if completed.returncode == 0 else ""


def tracked_inputs(module: str) -> list[Path]:
    fixed = [LAKE_DIR / name for name in ("lean-toolchain", "lakefile.toml", "lake-manifest.json", "registry.json")]
    return fixed + module_sources(module) + [AUDIT_TEMPLATE, Path(__file__).resolve()]


def build_receipt(report: Report) -> dict:
    owned = report.declarations
    return {
        "schema_version": 1,
        "created_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "verdict": report.verdict,
        "module": report.module,
        "git": {
            "commit": git("rev-parse", "HEAD") or None,
            "branch": git("branch", "--show-current") or None,
            # A receipt is evidence for the recorded commit only if the tree was clean.
            "tree_clean": git("status", "--porcelain") == "",
        },
        "platform": {"system": platform.system(), "machine": platform.machine(), "python": platform.python_version()},
        "toolchain": report.toolchain,
        "allowed_axioms": sorted(ALLOWED_AXIOMS),
        "sources": [
            {"path": path.relative_to(ROOT).as_posix(), "sha256_lf": sha256_text_file(path)}
            for path in tracked_inputs(report.module)
        ],
        "checks": [check.as_dict() for check in report.checks],
        "declarations": {
            "total": len(owned),
            "theorems": sum(1 for declaration in owned if declaration["kind"] == "theorem"),
            "named": sorted(declaration["name"] for declaration in owned if not is_auxiliary(declaration["name"])),
            "axioms_used": sorted({axiom for declaration in owned for axiom in declaration["axioms"]}),
        },
        "registry": report.registry,
        "commands": [command.as_dict() for command in report.commands],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--module", default=DEFAULT_MODULE, help="root module to verify (default: Conjectura)")
    parser.add_argument("--no-receipt", action="store_true", help="do not write a receipt")
    parser.add_argument("--show-fingerprints", action="store_true", help="print the current statement fingerprint of every registered theorem")
    args = parser.parse_args(argv)

    report = verify(module=args.module)
    for check in report.checks:
        print(f"[{check.status:>7}] {check.name}")
        for detail in check.details:
            print(f"          {detail}")
    if args.show_fingerprints:
        for entry in report.registry:
            print(f"{entry['name']}\n    statement:   {entry.get('statement')}\n    fingerprint: {entry.get('statement_fingerprint')}")

    if not args.no_receipt and args.module == DEFAULT_MODULE:
        receipt = build_receipt(report)
        RECEIPTS.mkdir(parents=True, exist_ok=True)
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        commit = (receipt["git"]["commit"] or "nocommit")[:10]
        suffix = "" if receipt["git"]["tree_clean"] else "-dirty"
        path = RECEIPTS / f"{stamp}-{commit}{suffix}-{report.verdict}.json"
        path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        print(f"receipt: {path.relative_to(ROOT).as_posix()}")

    print(f"VERDICT: {report.verdict}")
    return 0 if report.verdict == PASSED else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
