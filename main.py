"""Loading Screen Gold entry writer.

Writes the single 86-character loading-screen tip to /output/entry.txt.
The tip speaks to both the stressed developer and the AI coding agent:
the agent is not stuck, it is just waiting for the human to look away.
"""

from pathlib import Path

TIP = "Tip: Your agent is not stuck. It is politely waiting for you to stop watching it work."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TIP, encoding="utf-8")


if __name__ == "__main__":
    main()
