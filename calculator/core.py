# addition function
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

# subtraction function
def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

# multiplication function
def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

# division function
def divide(a, b):
    """Returns the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# test the calculator functions
def test_calculator():
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(2, 3) == 6
    assert divide(6, 3) == 2
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

if __name__ == "__main__":
    test_calculator()
    print("All tests passed.") # confirm all tests passed