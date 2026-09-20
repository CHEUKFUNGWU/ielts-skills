#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VALID_SKILLS = {
    "ielts-writing-task1",
    "ielts-writing-task2",
    "ielts-band8-vocabulary",
    "ielts-band8-study-plan",
}
VALID_PRIORITIES = {"critical", "standard"}


def main() -> None:
    data = json.loads((ROOT / "cases.json").read_text(encoding="utf-8"))
    cases = data.get("cases")
    assert data.get("version") == 1, "version must be 1"
    assert isinstance(cases, list) and len(cases) == 20, "expected exactly 20 cases"

    ids = [case.get("id") for case in cases]
    assert len(ids) == len(set(ids)), "case IDs must be unique"

    for case in cases:
        case_id = case.get("id", "<missing>")
        assert case.get("skill") in VALID_SKILLS, f"{case_id}: invalid skill"
        assert case.get("priority") in VALID_PRIORITIES, f"{case_id}: invalid priority"
        assert isinstance(case.get("mode"), str) and case["mode"], f"{case_id}: mode required"
        assert isinstance(case.get("request"), str) and case["request"].strip(), f"{case_id}: request required"
        for field in ("expected", "forbidden"):
            values = case.get(field)
            assert isinstance(values, list) and values, f"{case_id}: {field} must be non-empty"
            assert all(isinstance(value, str) and value.strip() for value in values), f"{case_id}: invalid {field} item"

    coverage = Counter(case["skill"] for case in cases)
    assert all(coverage[skill] >= 2 for skill in VALID_SKILLS), "each skill needs at least two cases"
    print(f"Validated {len(cases)} cases: " + ", ".join(f"{skill}={coverage[skill]}" for skill in sorted(coverage)))


if __name__ == "__main__":
    main()
