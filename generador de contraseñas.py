import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud = int(input("Ingrese la longitud de la contraseña deseada: "))

print("Tu contraseña segura es:", generar_contrasena(longitud))