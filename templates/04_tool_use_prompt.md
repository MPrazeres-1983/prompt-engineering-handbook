# Tool-use Prompt Template (When the assistant can call tools)

## Purpose
Make tool usage explicit and predictable.

Rules:
- Decide whether a tool is needed
- If needed, specify what to fetch and why
- After tool output, summarize and produce final answer

Output format:
- Tool plan: <tool + query>
- Result summary: <key findings>
- Final output: <structured answer>
