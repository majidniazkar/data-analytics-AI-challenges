#!/usr/bin/env python3
"""Check that every challenge folder is complete and its datasets are readable.

A missing statement is an error. A missing PDF or a dataset that has not been added
yet is reported as a warning, so the repository can be published while material is
still being filled in.

Run from the repository root:

    python scripts/validate_challenges.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

CHALLENGES = Path(__file__).resolve().parent.parent / "challenges"
DATA_SUFFIXES = {".csv", ".xlsx", ".xls"}


def check_challenge(folder: Path) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for one challenge folder."""
    errors: list[str] = []
    warnings: list[str] = []

    if not (folder / "README.md").is_file():
        errors.append("missing README.md (the challenge statement)")

    if not (folder / "challenge.pdf").is_file():
        warnings.append("no challenge.pdf - the original brief has not been added yet")

    data_dir = folder / "data"
    if not data_dir.is_dir():
        # Several challenges ask the student to source their own dataset.
        return errors, warnings

    datasets = [p for p in sorted(data_dir.iterdir()) if p.suffix.lower() in DATA_SUFFIXES]
    if not datasets:
        warnings.append("data/ exists but contains no .csv or .xlsx file yet")

    for dataset in datasets:
        reader = pd.read_csv if dataset.suffix.lower() == ".csv" else pd.read_excel
        try:
            frame = reader(dataset)
        except Exception as error:
            errors.append(f"{dataset.name} is unreadable: {error}")
            continue
        if frame.empty:
            errors.append(f"{dataset.name} has no rows")

    return errors, warnings


def main() -> int:
    folders = sorted(p for p in CHALLENGES.iterdir() if p.is_dir())
    if not folders:
        print(f"no challenge folders found under {CHALLENGES}")
        return 1

    failed = 0
    warned = 0
    for folder in folders:
        errors, warnings = check_challenge(folder)
        status = "FAIL" if errors else ("warn" if warnings else "ok  ")
        print(f"{status} {folder.name}")
        for problem in errors:
            print(f"       error: {problem}")
        for problem in warnings:
            print(f"       warn:  {problem}")
        failed += bool(errors)
        warned += bool(warnings) and not errors

    print(f"\n{len(folders)} challenges: {len(folders) - failed - warned} complete, "
          f"{warned} incomplete, {failed} invalid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
