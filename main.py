"""Loading Screen Gold: A Tip in 200 Characters (v2).

Writes the tip to /output/entry.txt, exactly as the competition expects.
One line, no trailing newline.
"""

from pathlib import Path

TIP = "Tip: If your agent says 'almost done' for the third time, it is already building a second project."


def main():
    if not 1 <= len(TIP) <= 200:
        raise ValueError(f"tip must be 1-200 characters, got {len(TIP)}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TIP, encoding="utf-8")


if __name__ == "__main__":
    main()
