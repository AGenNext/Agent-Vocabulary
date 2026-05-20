#!/usr/bin/env python3
"""Validate Agent-Vocabulary JSON-LD seed files.

This script intentionally performs structural validation without requiring
network access. It checks that every seed file is JSON, that vocabulary files
are DefinedTermSet objects, and that every entry in hasDefinedTerm is a
DefinedTerm with name and termCode.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED_DIR = ROOT / "seed"


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def validate_file(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))

    if data.get("@type") not in {"schema:DefinedTermSet", "DefinedTermSet"}:
        fail(f"{path}: root @type must be schema:DefinedTermSet")

    terms = data.get("hasDefinedTerm")
    if not isinstance(terms, list) or not terms:
        fail(f"{path}: hasDefinedTerm must be a non-empty list")

    seen_codes: set[str] = set()
    for index, term in enumerate(terms):
        if not isinstance(term, dict):
            fail(f"{path}: hasDefinedTerm[{index}] must be an object")
        if term.get("@type") not in {"schema:DefinedTerm", "DefinedTerm"}:
            fail(f"{path}: hasDefinedTerm[{index}].@type must be schema:DefinedTerm")
        name = term.get("name")
        term_code = term.get("termCode")
        if not isinstance(name, str) or not name:
            fail(f"{path}: hasDefinedTerm[{index}].name is required")
        if not isinstance(term_code, str) or not term_code:
            fail(f"{path}: hasDefinedTerm[{index}].termCode is required")
        if term_code in seen_codes:
            fail(f"{path}: duplicate termCode {term_code}")
        seen_codes.add(term_code)


def main() -> None:
    files = sorted(SEED_DIR.rglob("*.jsonld"))
    if not files:
        fail("no JSON-LD seed files found")
    for path in files:
        validate_file(path)
        print(f"ok: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
