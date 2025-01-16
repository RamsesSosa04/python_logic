def extraer_dominio_manual(url):
  """
  Extrae el nombre de dominio de una URL de forma manual (simplificada).

  Args:
    url: La URL como cadena de texto.

  Returns:
    El nombre de dominio como cadena de texto, o None si no se encuentra.
  """

  # Eliminar el protocolo (http://, https://) y cualquier cosa después del dominio
  parts = url.split('/')
  if len(parts) > 2:
      host = parts[2]
  else:
      return None

  # Eliminar el subdominio (www.) si existe
  parts = host.split('.')
  if len(parts) > 2:
      return parts[-2]
  else:
      return parts[0]

# Ejemplos de uso:
url1 = "http://github.com/carbonfive/raygun"
url2 = "http://www.zombie-bites.com"
url3 = "https://www.cnet.com"

print(extraer_dominio_manual(url1))  # Salida: github
print(extraer_dominio_manual(url2))  # Salida: zombie-bites
print(extraer_dominio_manual(url3))  # Salida: cnet