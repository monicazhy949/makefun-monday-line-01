"""Monday, Reviewed in One Line — entry program.

Writes a single-line review of my Monday to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "One star: my Monday alarm snoozed itself, my inbox hit 47 unread "
    "before coffee, and my 9 a.m. meeting introduced me to my own team."
)


def main() -> None:
    print(ENTRY)
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
