"""
  Adds two numbers and returns their sum in binary.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The sum of a and b in binary format as a string.
"""

def add_binary(a,b):
    num = a + b
    result = bin(num)[2:]
    return result
print(add_binary(5, 9))