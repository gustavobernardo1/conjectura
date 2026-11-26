"""Shared test configuration."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import verify_lean  # noqa: E402


@pytest.fixture(scope="session")
def root() -> Path:
    return ROOT


def pytest_collection_modifyitems(config, items):
    """Skip Lean tests, with the reason stated, when the toolchain is unavailable."""
    lake = verify_lean.find_tool("lake")
    mathlib_built = (ROOT / "formalization" / ".lake" / "packages" / "mathlib" / ".lake" / "build").is_dir()
    if lake and mathlib_built:
        return
    reason = "`lake` not found" if not lake else "Mathlib build products not found (run `lake exe cache get`)"
    skip = pytest.mark.skip(reason=f"Lean tests not run: {reason}")
    for item in items:
        if "lean" in item.keywords:
            item.add_marker(skip)
