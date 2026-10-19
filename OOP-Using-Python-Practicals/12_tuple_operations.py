"""Practical 12: Perform the required operations on tuples."""


def main() -> None:
    t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
    t2 = (11, 13, 15)
    midpoint = len(t1) // 2

    print("Original tuple t1:", t1)
    print("(a) First half:", *t1[:midpoint])
    print("    Second half:", *t1[midpoint:])
    print("(b) Even numbers:", tuple(number for number in t1 if number % 2 == 0))
    print("(c) t2 concatenated with t1:", t2 + t1)
    print("(d) Maximum value in t1:", max(t1))
    print("    Minimum value in t1:", min(t1))


if __name__ == "__main__":
    main()
