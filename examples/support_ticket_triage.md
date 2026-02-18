# Example: Support Ticket Triage

## Context
We receive a user report: "Login fails with 2FA, getting 403."

## Goal
Generate a triage response for support engineers.

## Constraints
- Ask for missing info first
- Provide immediate mitigation steps
- Suggest ownership routing (team)
- Keep it under 200 words

## Expected good output
- Clarifying questions (timestamp, device, browser, error details)
- Mitigation: clear cache, check 2FA device, verify account status
- Routing: auth/identity team if persists

## Evaluation notes
- Correctness: 2/3 (depends on system specifics)
- Constraint adherence: 3/3
- Actionability: 3/3
