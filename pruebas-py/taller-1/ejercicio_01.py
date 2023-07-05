""""
Escribe un programa que solicite al usuario ingresar su edad y luego determine si es mayor de edad o no utilizando una declaración if. Si la edad es mayor o igual a 18, muestra el mensaje "Eres mayor de edad", de lo contrario, muestra el mensaje "Eres menor de edad".
"""
import os

os.system("clear")

edad = int(input("ingresa tu edad: "))

if (edad >= 18) :
    print("Eres mayor de edad")
else :
    print("Eres menor de edad")