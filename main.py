"""The Houseplant Out-of-Office — make.fun entry (account A / overtheraa).

Writes one out-of-office auto-reply, as if from a fern ignored since
March, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "Out of office since March. I photosynthesized in silence for eight months. I'm on leave - literally. Do not water me."


def validate(line: str) -> str:
    """Enforce the gate: a single non-blank line of 1-120 characters."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 120:
        raise ValueError(f"entry is {len(line)} characters, over the 120 limit")
    if len(line) < 1:
        raise ValueError("entry must be at least 1 character")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
