"""Practical 06: Swap the first n characters of two strings."""


def swap_first_n(first: str, second: str, n: int) -> tuple[str, str]:
    """Exchange each string's first n characters while preserving each remainder."""
    if n < 0 or n > min(len(first), len(second)):
        raise ValueError("n must be between 0 and the length of the shorter string.")
    return second[:n] + first[n:], first[:n] + second[n:]


def main() -> None:
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")
    try:
        n = int(input("Enter n: "))
        new_first, new_second = swap_first_n(first, second, n)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    print("First string after swapping:", new_first)
    print("Second string after swapping:", new_second)


if __name__ == "__main__":
    main()
