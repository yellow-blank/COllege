"""Practical 10: Define a Point class and calculate distance between points."""
from math import hypot


class Point:
    """Represent a point in a two-dimensional coordinate plane."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x:g}, {self.y:g})"

    def distance(self, other: "Point") -> float:
        """Return the Euclidean distance from this point to another point."""
        return hypot(self.x - other.x, self.y - other.y)


def main() -> None:
    try:
        x1 = float(input("Enter x-coordinate of point 1: "))
        y1 = float(input("Enter y-coordinate of point 1: "))
        x2 = float(input("Enter x-coordinate of point 2: "))
        y2 = float(input("Enter y-coordinate of point 2: "))
    except ValueError:
        print("Please enter valid numeric coordinates.")
        return

    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    print("First object:", point1)
    print("Second object:", point2)
    print(f"Distance between the points: {point1.distance(point2):.3f}")


if __name__ == "__main__":
    main()
