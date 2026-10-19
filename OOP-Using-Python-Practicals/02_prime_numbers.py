"""Practical 02: Test primality and generate prime numbers."""
while True:
    def is_prime(number: int) -> bool:
        """Return True when number is prime."""
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        divisor = 3
        while divisor * divisor <= number:
            if number % divisor == 0:
                return False
            divisor += 2
        return True


    def primes_upto(limit: int) -> list[int]:
        """Return all primes less than or equal to limit."""
        return [number for number in range(2, limit + 1) if is_prime(number)]


    def first_n_primes(count: int) -> list[int]:
        """Return the first count prime numbers."""
        primes = []
        candidate = 2
        while len(primes) < count:
            if is_prime(candidate):
                primes.append(candidate)
            candidate += 1
        return primes


    def main() -> None:
        try:
            n = int(input("Enter a non-negative integer n: "))
            if n < 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
            return

        print(f"(a) Is {n} prime? {'Yes' if is_prime(n) else 'No'}")
        print(f"(b) Prime numbers up to {n}: {primes_upto(n)}")
        print(f"(c) First {n} prime number(s): {first_n_primes(n)}")


    if __name__ == "__main__":
        main()
