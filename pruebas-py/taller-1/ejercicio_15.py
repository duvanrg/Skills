"""
Escribe un programa que solicite al usuario ingresar una frase y luego cuente cuántas veces aparece la letra 'a' en la frase utilizando un bucle for.
"""
import os

os.system("clear")

cont = 0
frase = input("Ingrese una frase: ")

for c in frase:
    if c == "a":
        cont += 1 

print(cont)