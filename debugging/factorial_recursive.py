#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given number recursively.

    Parameters:
    - n (int): The number whose factorial is to be calculated.

    Return:
    - int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Extract the command-line argument and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
