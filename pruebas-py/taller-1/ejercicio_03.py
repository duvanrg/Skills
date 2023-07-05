"""
Escribir un programa que solicite al usuario ingresar un número entero y determine si es positivo, negativo o cero. Imprimir un mensaje correspondiente para cada caso.
"""
import os

os.system("clear")

num = int(input("ingrese un numero entero: "))

if num > 0:
    print(f"el numero {num} es positivo")
elif num < 0:
    print(f"el numero {num} es negativo")
else:
    print(f"el numero es {num}")


