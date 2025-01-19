def sumar_positivos(numeros):
  """
  Suma todos los números positivos en una lista.

  Args:
    numeros: Una lista de números.

  Returns:
    La suma de los números positivos, o 0 si no hay ninguno.
  """

  suma = 0
  for numero in numeros:
    if numero > 0:
      suma += numero
  return suma

# Ejemplo de uso:
lista_numeros = [1, -4, 7, 12]
resultado = sumar_positivos(lista_numeros)
print(resultado)  