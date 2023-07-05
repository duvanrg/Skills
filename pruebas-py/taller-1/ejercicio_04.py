"""
Desarrollar un programa que solicite al usuario ingresar un número y determine si es par. Si lo es, imprimir el mensaje "El número es par"; de lo contrario, no hacer nada.
"""
import os

os.system("clear")

num = int(input("ingrese un numero: "))

if num % 2 == 0:
    print(f"el numero {num} es par")


