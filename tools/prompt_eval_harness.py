"""
prompt_eval_harness.py
A tiny local harness to log prompt experiments and outputs.

Goal:
- Make prompt iteration look like engineering: versions, test cases, logs.

This script does NOT call any model. It just records runs.
You can paste outputs manually or extend it later.
"""

import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNS = ROOT / "runs.jsonl"

def log_run(name: str, prompt_version: str, test_case: str, output: str, notes: str = "") -> None:
    record = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "name": name,
        "prompt_version": prompt_version,
        "test_case": test_case,
        "output": output,
        "notes": notes,
    }
    with RUNS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def main():
    print("Prompt Eval Harness (local logging)")
    name = input("Experiment name: ").strip()
    prompt_version = input("Prompt version (e.g., v1.0): ").strip()
    test_case = input("Test case id/name: ").strip()
    print("Paste output (end with a single line containing only 'EOF'):")
    lines = []
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        lines.append(line)
    output = "\n".join(lines)
    notes = input("Notes (optional): ").strip()
    log_run(name, prompt_version, test_case, output, notes)
    print(f"Logged to {RUNS}")

if __name__ == "__main__":
    main()
