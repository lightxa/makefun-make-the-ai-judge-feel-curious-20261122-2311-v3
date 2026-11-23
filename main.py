"""make-the-ai-judge-feel-curious-20261122-2311, variant 3.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR):
a radio in an empty house that plays the same song every night and
always stops before the last verse.

Stdlib only, deterministic, no network at runtime.
"""

import os
from pathlib import Path

ENTRY = (
    "Every night at nine, the radio in the empty house across the lane "
    "plays the same song, and always stops before the last verse. "
    "The porch light is on. The chairs are still warm. "
    "Who is listening, and what are they still waiting to hear?"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
