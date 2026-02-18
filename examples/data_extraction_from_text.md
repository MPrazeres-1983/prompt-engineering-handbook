# Example: Data Extraction from Text (Schema-driven)

## Goal
Extract structured fields from free text.

## Constraints
- Output MUST be JSON
- Missing fields must be null
- No extra keys

## Schema
{
  "customer_name": string|null,
  "issue_type": string|null,
  "urgency": "low"|"medium"|"high"|null,
  "timestamp": string|null
}

## Prompt pattern
- Provide schema
- Provide examples
- Enforce “no extra keys”
