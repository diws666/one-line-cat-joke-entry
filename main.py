"""Make.fun bounty entry builder for "The One-Line Cat Joke That Lands".

Writes the one-line cat joke to the output directory so it can be bundled
and submitted to the bounty.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The one-line cat joke entry (exactly as submitted to the bounty).
ENTRY_LINE = "The cat knocked the glass off the table, looked me in the eye, and did it again. Management material."


def write_entry(line: str, output_dir: str) -> str:
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main() -> None:
    write_entry(ENTRY_LINE, OUTPUT_DIR)


if __name__ == "__main__":
    main()
