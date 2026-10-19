"""Practical 08: Cube only even integers in a list, using two approaches."""
import ast


def even_cubes_with_loop(values: list) -> list[int]:
    result = []
    for value in values:
        # bool is a subclass of int in Python, so exclude it explicitly.
        if isinstance(value, int) and not isinstance(value, bool) and value % 2 == 0:
            result.append(value ** 3)
    return result


def even_cubes_with_comprehension(values: list) -> list[int]:
    return [value ** 3 for value in values
            if isinstance(value, int) and not isinstance(value, bool) and value % 2 == 0]


def main() -> None:
    raw_values = input("Enter a Python list (e.g. [2, 'hi', 3, 4.5, 6]): ")
    try:
        values = ast.literal_eval(raw_values)
        if not isinstance(values, list):
            raise ValueError("The input must be a list.")
    except (ValueError, SyntaxError) as error:
        print(f"Invalid list: {error}")
        return

    print("(a) Cubes using a for loop:", even_cubes_with_loop(values))
    print("(b) Cubes using list comprehension:", even_cubes_with_comprehension(values))


if __name__ == "__main__":
    main()
