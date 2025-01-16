from urllib.parse import urlparse

def extraer_dominio(url):
  """
  Extrae el nombre de dominio de una URL.

  Args:
    url: La URL como cadena de texto.

  Returns:
    El nombre de dominio como cadena de texto.
  """

  # Analiza la URL utilizando urllib.parse
  parsed_uri = urlparse(url)
  # Extrae el netloc (nombre de red), que incluye el subdominio y el dominio
  result = parsed_uri.netloc
  # Elimina el subdominio si existe (por ejemplo, 'www.')
  result = result.split('.')[-2]
  return result

# Ejemplos de uso:
url1 = "http://github.com/carbonfive/raygun"
url2 = "http://www.zombie-bites.com"
url3 = "https://www.cnet.com"

print(extraer_dominio(url1))  # Salida: github
print(extraer_dominio(url2))  # Salida: zombie-bites
print(extraer_dominio(url3))  # Salida: cnet