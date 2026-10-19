"""Practical 13: Validate a user's name using custom exceptions."""


class DigitsInNameError(ValueError):
    """Raised when a name contains one or more digits."""


class SpecialCharactersInNameError(ValueError):
    """Raised when a name contains punctuation or symbols."""


def validate_name(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    if any(character.isdigit() for character in name):
        raise DigitsInNameError("A name must not contain digits.")
    if any(not (character.isalpha() or character == " ") for character in name):
        raise SpecialCharactersInNameError(
            "A name may contain letters and spaces only; special characters are not allowed."
        )
    return name


def main() -> None:
    entered_name = input("Enter your name: ")
    try:
        valid_name = validate_name(entered_name)
    except DigitsInNameError as error:
        print("Invalid name:", error)
    except SpecialCharactersInNameError as error:
        print("Invalid name:", error)
    except ValueError as error:
        print("Invalid name:", error)
    else:
        print("Name accepted:", valid_name)


if __name__ == "__main__":
    main()
