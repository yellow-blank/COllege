    """Practical 01: Find the roots of a quadratic equation."""
import cmath
    
while True:    
    def find_roots(a: float, b: float, c: float) -> tuple[complex, complex] | tuple[float, ...] | tuple[str]:
        """Return the roots of ax^2 + bx + c = 0, including complex roots."""
        if a == 0:
            if b == 0:
                if c == 0:
                    return ("Every value of x is a solution.",)
                return ("No solution exists.",)
            return (-c / b,)
    
        discriminant = b * b - 4 * a * c
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return root1, root2
    
    
    def display_number(value: complex) -> str:
        """Display real roots without an unnecessary imaginary part."""
        if abs(value.imag) < 1e-12:
            return f"{value.real:g}"
        return f"{value.real:g}{value.imag:+g}j"
    
    
    def main() -> None:
        print("Find the roots of ax² + bx + c = 0")
        try:
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
        except ValueError:
            print("Please enter valid numbers.")
            return
    
        roots = find_roots(a, b, c)
        if len(roots) == 1 and isinstance(roots[0], str):
            print(roots[0])
        elif a == 0:
            print(f"The linear equation has solution x = {roots[0]:g}")
        else:
            print(f"Root 1 = {display_number(roots[0])}")
            print(f"Root 2 = {display_number(roots[1])}")
    
    
    if __name__ == "__main__":
        main()
