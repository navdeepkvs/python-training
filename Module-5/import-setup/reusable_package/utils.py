def greet(name):
    return f"Hello, {name}"


def find_max(values):
    """Return the maximum value from a list of numbers."""
    if not values:
        raise ValueError("find_max() arg is an empty list")
    return max(values)


def count_characters(text):
    """Return the number of characters in the given string."""
    return len(text)


def reverse_string(text):
    """Return the reversed version of the input string."""
    return text[::-1]


def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sum_list(numbers):
    """Return the sum of all numbers in the list."""
    return sum(numbers)


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    