# Behaviour evaluations

These cases test whether the IELTS skills make sound decisions. They do not require exact wording.

## Run a case

1. Start a fresh agent session with the named skill installed.
2. Send the `request` and any supplied `context` from `cases.json`.
3. Compare the response with every item in `expected` and `forbidden`.
4. Mark the case as passed only when all expected behaviours are present and all forbidden behaviours are absent.
5. Record a short quotation from the response as evidence for each decision.

Use a fresh session so earlier prompts do not influence the result. Do not show the model the expectations before it answers.

## Result format

```text
Case: task2-missing-prompt
Model: <model and version>
Result: PASS | FAIL

Expected
- PASS: <requirement> | Evidence: "<short quote>"

Forbidden
- PASS: <prohibition> | Evidence: "<short quote or not observed>"

Notes: <optional>
```

The `critical` priority marks failures that can produce unsupported scores, invented data or materially misleading teaching. Report critical results separately from the remaining cases instead of hiding them inside one average.

## Validate the case file

The validator checks structure, IDs and coverage. It does not call a model.

```bash
python3 evals/validate_cases.py
```

Add a new case when a real failure reveals a distinct decision problem. Do not add several cases that differ only in topic wording.
