# Methodology (Applied Research)

This project treats prompting as an engineering activity with:
- clear requirements (constraints, format, tone, safety)
- controlled variables (system prompt, context, temperature, tool access)
- evaluation criteria (rubric)
- reproducible test cases (examples)

## Process
1) Define the task and constraints
2) Draft a baseline prompt (minimal)
3) Add structure:
   - roles and responsibilities
   - input schema
   - output schema
   - refusal/safety policy
4) Run test cases:
   - normal inputs
   - ambiguous inputs
   - adversarial inputs (prompt injection)
5) Evaluate using the rubric
6) Iterate and document changes in the changelog

## What this repository provides
- Templates to standardize structure
- Examples to act as test cases
- A rubric to evaluate quality consistently
- A small harness to log and compare outputs over time
