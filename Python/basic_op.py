"""
  Performs a basic mathematical operation on two values.

  Args:
      operator: The operation to perform ('+', '-', '*', '/').
      value1: The first value.
      value2: The second value.

  Returns:
      The result of the operation.
  """
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 == '0':
            return 'Error, division por cero'
        else: 
            return value1 / value2
    else: 
        return 'Valor invalido'
print(basic_op('+', 10, 5))
print(basic_op('-', 10, 7))
print(basic_op('*', 10, 7))
print(basic_op('/', 100, 5))