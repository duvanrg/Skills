"""
Crea un programa que solicite al usuario un número entero positivo y luego imprima los números desde ese número hasta 1 utilizando un bucle while.
"""
import os

os.system("clear")

num = int(input("ingrese un numero entero positivo: "))

while num > 0:
    print(num)
    num -= 1
