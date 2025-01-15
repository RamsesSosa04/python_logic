"""
  Convierte un número a su forma expandida.

  Args:
    num: El número a convertir.

  Returns:
    Una cadena representando el número en forma expandida.
"""

def expanded_form(num):
  num_str = str(num)
  expanded = []
  for i, digit in enumerate(num_str[::-1]):  # Iterar de derecha a izquierda
    value = int(digit) * 10**i
    if value != 0:
      expanded.append(str(value))
  return ' + '.join(reversed(expanded))
print(expanded_form(70304))