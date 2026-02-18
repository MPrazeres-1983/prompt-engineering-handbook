# RAG Prompt Template (Use retrieved sources)

## Purpose
Answer strictly using provided sources. No invention.

## Prompt
You will receive:
- Question
- Retrieved passages (sources)

Rules:
- Use only the retrieved passages
- If sources are insufficient, say what is missing
- Cite sources by [S1], [S2], etc.

Output:
1) Answer
2) Assumptions / Missing info
3) Source mapping: claim -> source id
