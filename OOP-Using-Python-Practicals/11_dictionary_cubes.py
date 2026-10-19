"""Practical 11: Print a dictionary whose keys 1 through 5 map to their cubes."""


def print_cube_dictionary() -> None:
    cubes = {number: number ** 3 for number in range(1, 6)}
    print(cubes)


if __name__ == "__main__":
    print_cube_dictionary()
