"""
  Reemplaza los dígitos menores que 5 por '0' y los mayores o iguales a 5 por '1'.

  Args:
    cadena: La cadena de dígitos a modificar.

  Returns:
    La cadena modificada.
"""
def fake_bin(x):
    result = ""
    for digit in x:
        if int(digit) < 5:
            result += "0"
        else:
            result += "1"
    return result

x = "941397315975486433143425066"
result = fake_bin(x)
print(result)
