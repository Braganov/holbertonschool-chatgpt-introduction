#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid an infinite loop
    return result

# Check if a command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

# Calculate and print the factorial
try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Please provide a valid integer.")
