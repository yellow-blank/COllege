"""Practical 09: Count file contents, calculate character frequency, and split lines."""
from pathlib import Path


def character_frequencies(text: str) -> dict[str, int]:
    frequency: dict[str, int] = {}
    for character in text:
        frequency[character] = frequency.get(character, 0) + 1
    return frequency


def main() -> None:
    script_directory = Path(__file__).resolve().parent
    sample_path = script_directory / "sample.txt"
    entered_path = input(
        f"Enter a file path, or press Enter to use {sample_path.name}: "
    ).strip()
    file_path = Path(entered_path).expanduser() if entered_path else sample_path
    if not file_path.is_absolute():
        file_path = Path.cwd() / file_path

    try:
        contents = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Could not read the file: {error}")
        return

    words = contents.split()
    lines = contents.splitlines(keepends=True)
    print(f"\nFile: {file_path}")
    print("(a) Total characters:", len(contents))
    print("    Total words:", len(words))
    print("    Total lines:", len(contents.splitlines()))

    print("(b) Frequency of each character:")
    for character, count in character_frequencies(contents).items():
        print(f"    {character!r}: {count}")

    print("(c) Words in reverse order:")
    print(" ".join(reversed(words)))

    # Lines are numbered from 1: even lines go to File1, odd lines to File2.
    even_lines = [line for line_number, line in enumerate(lines, start=1)
                  if line_number % 2 == 0]
    odd_lines = [line for line_number, line in enumerate(lines, start=1)
                 if line_number % 2 == 1]
    (script_directory / "File1").write_text("".join(even_lines), encoding="utf-8")
    (script_directory / "File2").write_text("".join(odd_lines), encoding="utf-8")
    print("(d) Even-numbered lines saved to practicals/File1.")
    print("    Odd-numbered lines saved to practicals/File2.")


if __name__ == "__main__":
    main()
