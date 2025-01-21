"""
  Calcula el volumen de un cuboide.

  Args:
    largo: La longitud del cuboide.
    ancho: El ancho del cuboide.
    alto: La altura del cuboide.

  Returns:
    El volumen del cuboide.
"""
def calcular_volumen(largo, ancho, alto):
    volumen = largo * ancho * alto
    return volumen

print(calcular_volumen(5,10,2))
