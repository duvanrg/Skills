"""
Escribe un programa que solicite al usuario ingresar un número y luego muestre la tabla de multiplicar de ese número del 1 al 10
"""
import os

os.system("clear")

num = int(input("Ingrese un número: "))

for i in range(0,10):
    print(f"{num} x {i+1} = {num*(i+1)}")
