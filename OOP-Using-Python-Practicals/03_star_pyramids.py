"""Practical 03: Print a star pyramid and its reverse pyramid."""


def main() -> None:
    rows = 5

    # Print the pyramid: 1, 3, 5, 7, 9 stars.
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

    print()  # Separate the two patterns, as shown in the assignment sheet.

    # Print the reverse pyramid: 9, 7, 5, 3, 1 stars.
    for i in range(rows - 1, -1, -1):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))


if __name__ == "__main__":
    main()
