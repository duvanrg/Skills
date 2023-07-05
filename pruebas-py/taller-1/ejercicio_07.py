"""
Escribe un programa que solicite al usuario ingresar una contraseña y verifique si es correcta. Si la contraseña
ingresada es "secreto123", muestra el mensaje "Acceso concedido". Si la contraseña es diferente, muestra el
mensaje "Acceso denegado".
"""
import os

os.system("clear")

contraseña = "secreto123"
psw = input("Ingrese su contraseña")

if psw == contraseña:
    print("Acceso concedido (>‿◠)")
else:
    print("Acceso denegado (˘︹˘)")


