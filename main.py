def calculate_factorial(n):
    if n == 0:
        return 0

    return n * calculate_factorial(n - 1)


def display_factorial(n):
    print(f"The factorial of {n} is {calculate_factorial(n)}")


def main():
    display_factorial(6)
