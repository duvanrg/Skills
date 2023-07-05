"""
Crea un programa que solicite al usuario ingresar una palabra y luego muestre cada letra de la palabra en una línea separada utilizando un bucle for
"""
import os

os.system("clear")

word = str(input("Ingrese una palabra: "))

for c in word:
    print(c)
