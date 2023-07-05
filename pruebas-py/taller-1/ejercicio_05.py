"""
Crea un programa que solicite al usuario ingresar una contraseña y verifique si
cumple con los siguientes requisitos: debe tener al menos 8 caracteres y contener al
menos un número. Si la contraseña cumple con los requisitos, muestra el mensaje
"Contraseña válida". De lo contrario, muestra el mensaje "Contraseña inválida".
"""
import os

os.system("clear")

psw = input("ingrese una nueva contraseña: ")
aprov = 0 

if (len(psw) >= 8):
    for c in psw:
        if (c >= '0' and c <= '9'):
            aprov = 1
            break

if (aprov == 1):
    print("Contraseña valida (>‿◠)")
else :
    print("Contraseña invalida (˘︹˘)")


