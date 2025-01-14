"""
  Multiplica un número por 50 y le suma 6. Si el valor es una cadena, devuelve "Error".

  Args:
    valor: El valor a procesar.

  Returns:
    El resultado de la operación o "Error" si el valor no es numérico.
"""

def multiplicar_y_sumar(a):
    try:
        resultado = int(a) * 50 + 6
        return resultado
    except ValueError:
        return "error"

# Ejemplos de uso:
print(multiplicar_y_sumar(50))  # Imprime: 156
print(multiplicar_y_sumar("hola"))  # Imprime: Error