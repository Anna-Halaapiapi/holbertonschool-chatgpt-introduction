#!/usr/bin/python3
import sys


def factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n = n - 1  # decrement for loop
    return result


if len(sys.argv) != 2:  # error handling
    print("Usage: ./factorial.py <non-negative integer>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if (number < 0):  # error handling
        print("Error: negative number used.")
        sys.exit(1)

except ValueError:
    print("Error: input must be an integer")
    sys.exit(1)

f = factorial(int(number))
print(f)
