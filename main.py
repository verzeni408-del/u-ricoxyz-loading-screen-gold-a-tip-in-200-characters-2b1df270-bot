"""A tiny loading-screen tip writer for the make.fun bounty.

The whole job: hold one short tip in memory, sanity-check its
length, then drop it — with no trailing newline — into the
absolute output path the harness reads. One sentence, one file,
no fuss.
"""

from pathlib import Path

TIP = "Tip: The bar stuck at 99% means your agent is reading the same error for the fourth time, hoping it changes."
DEST = Path("/output/entry.txt")


def main() -> None:
    text = TIP.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"tip must be 1-200 chars, got {len(text)}")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
