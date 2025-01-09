"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in 
between them.
The output should be two capital letters with a dot separating them.
It should look like this:
Sam Harris => S.H
"""
def obtener_nombre(nombre):
    nombre, apellido = nombre.split()
 
    iniciales = f"{nombre[0].upper()}.{apellido[0].upper()}."
    return iniciales

print(obtener_nombre("Ramses Sosa"))  
print(obtener_nombre("Aylyn Perez"))  
    