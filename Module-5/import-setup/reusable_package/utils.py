def greet(name):
    return f"Hello, {name}"


def find_max(values):
    """Return the maximum value from a list of numbers."""
    if not values:
        raise ValueError("find_max() arg is an empty list")
    return max(values)
    