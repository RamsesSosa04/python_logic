"""
  Multiplica un número por 8 si es par y por 9 si es impar.

  Args:
    number: El número a multiplicar.

  Returns:
    El resultado de la multiplicación.
"""
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
print(simple_multiplication(8))