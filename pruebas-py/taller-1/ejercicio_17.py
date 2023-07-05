"""
Crea un programa que solicite al usuario ingresar un número y luego muestre la suma de los dígitos
de ese número utilizando un bucle while
"""
import os

os.system("clear")

suma = 0
num = int(input("Ingrese un numero de mas de dos digitos: "))

for i in str(num):
    suma += int(i)

print(f"la suma de los digitos del numero {num} es:  {suma}")

