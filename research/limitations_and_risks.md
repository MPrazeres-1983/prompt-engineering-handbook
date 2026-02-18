# Limitations and Risks

## Limitations
- Prompting quality depends on the underlying model capabilities.
- No single prompt is optimal for all contexts: tool access, latency, and cost matter.
- Evaluation rubrics reduce subjectivity but do not eliminate it.

## Risks
- **Prompt injection:** untrusted text may override instructions.
- **Data leakage:** copying real logs or customer data into prompts is dangerous.
- **Overconfidence:** models can be fluent while wrong.

## Mitigations
- Use strict output schemas and guardrails.
- Treat external text as untrusted input.
- Require “I don’t know” behavior when uncertain.
- Evaluate with stable test cases and compare versions.
