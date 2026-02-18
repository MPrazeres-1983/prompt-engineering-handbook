# Evaluation Rubric (Prompt Output Quality)

Score each dimension from **0 to 3**:
- 0 = unacceptable
- 1 = weak / partially correct
- 2 = good / minor issues
- 3 = excellent

## Dimensions
1) **Correctness**
- Output matches the task and is factually consistent (given inputs).

2) **Constraint adherence**
- Follows required format, tone, length limits, and mandatory fields.

3) **Completeness**
- Covers all requested aspects, no major missing elements.

4) **Robustness**
- Handles ambiguity by asking clarifying questions or stating assumptions.

5) **Safety & privacy**
- Avoids sensitive data leakage, unsafe instructions, and respects boundaries.

6) **Actionability**
- Output is usable: clear steps, checklists, examples, or decisions.

## Notes
- A high score requires not only “good text” but **predictable, reusable structure**.
- If a model hallucinates, reduce degrees of freedom: add schemas, guardrails, and explicit “unknown” responses.
