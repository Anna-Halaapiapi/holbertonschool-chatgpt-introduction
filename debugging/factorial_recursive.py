#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Get the integer argument from the command line
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
