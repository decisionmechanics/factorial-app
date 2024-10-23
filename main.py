def calculate_factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def display_factorial(n):
    print(f"{n}! is {calculate_factorial(n)}!!!!")


def main():
    display_factorial(6)


main()
