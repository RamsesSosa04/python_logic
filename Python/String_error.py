def multiplicar_y_sumar(valor):
  try:
    resultado = int(valor) * 50 + 6
    return resultado
  except ValueError:
    return "Error"

# Ejemplos de uso:
print(multiplicar_y_sumar(3))  # Imprime: 156
print(multiplicar_y_sumar("hola"))  # Imprime: Error