"""
  Divide una cadena en una lista de palabras.

  Args:
    cadena: La cadena de texto a dividir.

  Returns:
    Una lista con las palabras de la cadena.
  """
def string_to_array(s):
    array = s.split(' ')
    return array

print(string_to_array('I love arrays they are my favorite'))