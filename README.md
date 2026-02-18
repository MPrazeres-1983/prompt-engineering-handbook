# Prompt Engineering Handbook (Applied Playbook + Research Artefacts)

A practical prompt engineering handbook (PDF) plus reusable templates, evaluated examples, and a lightweight evaluation harness.
This repository is intentionally structured like **applied research**: it includes a methodology, an evaluation rubric, and reproducible examples.

## Why this exists
Most “prompting guides” are opinion-heavy and hard to operationalize. This project focuses on:
- **Repeatability:** templates you can reuse
- **Evaluation:** a rubric and an evaluation prompt to reduce “it worked once” outcomes
- **Safety:** practical guardrails (privacy, injection resistance, constraints)
- **Real workflows:** examples that map to engineering work (support triage, SQL, extraction)

## What’s inside
- **The book (PDF):** see [`/book`](./book)
- **Research artefacts:** methodology, rubric, dataset-style examples in [`/research`](./research)
- **Templates:** reusable prompt skeletons in [`/templates`](./templates)
- **Examples:** worked examples with constraints and evaluation notes in [`/examples`](./examples)
- **Tools:** a small local evaluation harness in [`/tools`](./tools) (optional)

## Quick start (2 minutes)
1) Read the book: [`/book/Engenharia_de_Prompts_O_Codigo_Oculto.pdf`](./book/Engenharia_de_Prompts_O_Codigo_Oculto.pdf)
2) Copy a template: [`/templates/01_system_prompt.md`](./templates/01_system_prompt.md)
3) Compare with an example: [`/examples/sql_query_assistant.md`](./examples/sql_query_assistant.md)
4) Evaluate outputs using the rubric: [`/research/evaluation_rubric.md`](./research/evaluation_rubric.md)

## Evaluation philosophy
Prompting is an interface design problem. Good prompts:
- enforce constraints
- reduce ambiguity
- produce consistent outputs
- fail safely
- are testable (with rubrics / checklists)

See the full methodology in [`/research/methodology.md`](./research/methodology.md).

## License
Text and templates are published under **CC BY-NC 4.0** (Attribution, Non-Commercial).
See [`LICENSE`](./LICENSE).

## Contact
- LinkedIn: https://www.linkedin.com/in/mario-prazeres/
- GitHub: https://github.com/MPrazeres-1983
