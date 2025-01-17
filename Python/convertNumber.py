def digitize(n):
  """
  Converts a non-negative integer into a list of its digits in reverse order.

  Args:
    n: The non-negative integer.

  Returns:
    A list of integers representing the digits of n in reverse order.
  """
  if n == 0:
    return [0]
  digits = []
  while n > 0:
    digits.append(n % 10)
    n //= 10
  return digits

# Example usage:
number = 35231
reversed_digits = digitize(number)
print(reversed_digits)  # Output: [1, 3, 2, 5, 3]