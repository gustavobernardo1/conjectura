"""Exhaustive exact test of the Collins–Shor peak-location conjecture on all trees of given orders.

For every isomorphism class of trees of order n the script computes the integer
sequence s_k = 2^k |delta_k| (k = 0..n-2), which is 2^(n-2) times the sequence
of normalized coefficients, and records where its maximum is attained. It also
re-checks two known facts on every tree as guards against computational error:

* Graham–Pollak: d_0(T) = n - 1, i.e. s_0 = (n - 1) 2^(n-2);
* unimodality of s_0, ..., s_{n-2} (Aalipour et al., Theorem 2.1).

A tree violates the conjecture (strong reading) if some maximizing index lies
outside [floor(n/2), ceil(n - n/sqrt(5))].

Usage:
    python experiments/CJ-0001-collins-shor-peak/exhaustive.py --min-order 3 --max-order 20 \
        --workers 6 --out experiments/CJ-0001-collins-shor-peak/results/exhaustive-03-20.json
"""

from __future__ import annotations

import argparse
import json
import multiprocessing
import platform
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import distpoly  # noqa: E402

CHUNK = 2000
MAX_EXAMPLES = 5


def process_chunk(chunk: list[bytes]) -> dict:
    histogram: Counter = Counter()
    violations: list[list[int]] = []
    guard_failures: list[list[int]] = []
    extremes: dict[str, tuple[int, list[int]]] = {}
    for raw in chunk:
        layout = list(raw)
        n = len(layout)
        low, high = distpoly.conjectured_interval(n)
        sequence = distpoly.scaled_coefficients(distpoly.parents_from_layout(layout))
        peaks = distpoly.peak_indices(sequence)
        histogram[tuple(peaks)] += 1
        first, last = peaks[0], peaks[-1]
        if first < low or last > high:
            violations.append(layout)
        unimodal = all(sequence[i] <= sequence[i + 1] for i in range(first)) and all(
            sequence[i] >= sequence[i + 1] for i in range(last, n - 2)
        )
        if sequence[0] != (n - 1) << (n - 2) or not unimodal or peaks != list(range(first, last + 1)):
            guard_failures.append(layout)
        if "min" not in extremes or first < extremes["min"][0]:
            extremes["min"] = (first, layout)
        if "max" not in extremes or last > extremes["max"][0]:
            extremes["max"] = (last, layout)
    return {"histogram": histogram, "violations": violations, "guard_failures": guard_failures, "extremes": extremes}


def chunks(order: int):
    batch: list[bytes] = []
    for layout in distpoly.layouts(order):
        batch.append(bytes(layout))
        if len(batch) == CHUNK:
            yield batch
            batch = []
    if batch:
        yield batch


def run_order(order: int, pool) -> dict:
    started = time.monotonic()
    histogram: Counter = Counter()
    violations: list[list[int]] = []
    guard_failures: list[list[int]] = []
    min_peak, max_peak = order, -1
    min_examples: list[list[int]] = []
    max_examples: list[list[int]] = []
    results = pool.imap_unordered(process_chunk, chunks(order)) if pool else map(process_chunk, chunks(order))
    for result in results:
        histogram.update(result["histogram"])
        violations.extend(result["violations"])
        guard_failures.extend(result["guard_failures"])
        for key, examples, better in (("min", min_examples, lambda a, b: a < b), ("max", max_examples, lambda a, b: a > b)):
            if key not in result["extremes"]:
                continue
            value, layout = result["extremes"][key]
            current = min_peak if key == "min" else max_peak
            if better(value, current):
                examples.clear()
                if key == "min":
                    min_peak = value
                else:
                    max_peak = value
            if value == (min_peak if key == "min" else max_peak) and len(examples) < MAX_EXAMPLES:
                examples.append(layout)
    low, high = distpoly.conjectured_interval(order)
    trees = sum(histogram.values())
    path = distpoly.peak_indices(distpoly.scaled_coefficients(distpoly.path_parents(order)))
    star = distpoly.peak_indices(distpoly.scaled_coefficients(distpoly.star_parents(order)))
    return {
        "order": order,
        "trees": trees,
        "trees_expected_A000055": distpoly.A000055[order],
        "enumeration_count_matches": trees == distpoly.A000055[order],
        "conjectured_interval": [low, high],
        "min_peak": min_peak,
        "max_peak": max_peak,
        "peak_histogram": {",".join(map(str, key)): value for key, value in sorted(histogram.items())},
        "trees_with_tied_maximum": sum(value for key, value in histogram.items() if len(key) > 1),
        "violations": len(violations),
        "violating_layouts": violations[:50],
        "guard_failures": len(guard_failures),
        "path_peak": path,
        "star_peak": star,
        "examples_min_peak_layouts": min_examples,
        "examples_max_peak_layouts": max_examples,
        "seconds": round(time.monotonic() - started, 1),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--min-order", type=int, default=3)
    parser.add_argument("--max-order", type=int, required=True)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    if args.max_order >= len(distpoly.A000055):
        parser.error("no reference tree count for this order")

    import flint
    import networkx

    report = {
        "experiment": "CJ-0001 exhaustive peak location",
        "statement_tested": "every maximizing index k of d_0..d_{n-2} satisfies floor(n/2) <= k <= ceil(n - n/sqrt(5))",
        "arithmetic": "exact integers (python-flint characteristic polynomial)",
        "versions": {"python": platform.python_version(), "python-flint": flint.__version__, "networkx": networkx.__version__},
        "workers": args.workers,
        "orders": [],
    }
    pool = multiprocessing.Pool(args.workers) if args.workers > 1 else None
    try:
        for order in range(args.min_order, args.max_order + 1):
            entry = run_order(order, pool)
            report["orders"].append(entry)
            print(
                f"n={order:>2} trees={entry['trees']:>9} interval={entry['conjectured_interval']} "
                f"peaks=[{entry['min_peak']},{entry['max_peak']}] ties={entry['trees_with_tied_maximum']} "
                f"violations={entry['violations']} guards={entry['guard_failures']} "
                f"count_ok={entry['enumeration_count_matches']} {entry['seconds']}s",
                flush=True,
            )
    finally:
        if pool:
            pool.close()
            pool.join()
    report["total_trees"] = sum(entry["trees"] for entry in report["orders"])
    report["total_violations"] = sum(entry["violations"] for entry in report["orders"])
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {args.out}")
    ok = all(entry["enumeration_count_matches"] and entry["guard_failures"] == 0 for entry in report["orders"])
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
