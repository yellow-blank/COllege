"""Practical 05: Perform common operations on a string."""


def require_one_character(prompt: str) -> str:
    value = input(prompt)
    if len(value) != 1:
        raise ValueError("Please enter exactly one character.")
    return value


def main() -> None:
    text = input("Enter a string: ")
    try:
        character = require_one_character("Character to count: ")
        old_character = require_one_character("Character to replace: ")
        new_character = require_one_character("Replacement character: ")
    except ValueError as error:
        print(error)
        return

    print(f"(a) Frequency of {character!r}: {text.count(character)}")
    print(f"(b) Replace {old_character!r} with {new_character!r}: "
          f"{text.replace(old_character, new_character)}")
    print(f"(c) Remove first {character!r}: {text.replace(character, '', 1)}")
    print(f"(d) Remove all {character!r}: {text.replace(character, '')}")


if __name__ == "__main__":
    main()
