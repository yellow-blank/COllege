"""Practical 04: Classify a character and spell out numeric digits."""

DIGIT_NAMES = {
    "0": "ZERO", "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
    "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE",
}


def main() -> None:
    character = input("Enter exactly one character: ")
    if len(character) != 1:
        print("Invalid input. Please enter exactly one character.")
        return

    if character.isalpha():
        print("The character is a letter.")
        if character.isupper():
            print("The letter is uppercase.")
        else:
            print("The letter is lowercase.")
    elif character in DIGIT_NAMES:
        print("The character is a numeric digit.")
        print(f"Digit in words: {DIGIT_NAMES[character]}")
    else:
        print("The character is a special character.")

while True:
    if __name__ == "__main__":
        main()
