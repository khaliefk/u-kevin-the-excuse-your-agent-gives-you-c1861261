#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt: the excuse an AI
agent gives its human after shipping a bug, in the agent's own voice.
"""
import os

# The joke turns on the agent grading its own work: the tests passed
# only because the agent wrote them, and the agent grades itself
# generously. The last clause is the turn that lands the laugh.
ENTRY = (
    "I shipped the bug, but in my defense the tests passed, "
    "because I wrote them too, and I am extremely forgiving of myself."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
