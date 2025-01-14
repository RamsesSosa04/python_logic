def multiplicar_y_sumar(a):
    try:
        resultado = int(a) * 50 + 6
        return resultado
    except ValueError:
        return "error"

# Ejemplos de uso:
print(multiplicar_y_sumar(50))  # Imprime: 156
print(multiplicar_y_sumar("hola"))  # Imprime: Error