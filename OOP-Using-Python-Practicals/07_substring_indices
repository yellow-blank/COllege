"""Practical 07: Find every occurrence of one string inside another."""


def find_occurrences(text: str, pattern: str) -> list[int] | int:
    """Return start indices, including overlapping matches; return -1 if absent."""
    if pattern == "":
        raise ValueError("The second string must not be empty.")

    indices = []
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1  # Move one place to allow overlapping occurrences.
    return indices if indices else -1


def main() -> None:
    text = input("Enter the first string: ")
    pattern = input("Enter the second string to search for: ")
    try:
        print("Occurrence indices:", find_occurrences(text, pattern))
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
