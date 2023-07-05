"""
Construya un algoritmo en Python, que permita ingresar la información de un empleado e imprima el nombre, los apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre
*Teléfono
*Año de ingreso a la empresa
*Apellidos
*Edad.
"""
import os

os.system("clear")

añoActual = 2023
print("ingrese los datos del empleado")
nombre = str(input("nombre: "))
Apellidos = str(input("Apellidos: "))
telefono = str(input("telefono: "))
ingreso = int(input("Año de ingreso: "))
edad = int(input("edad: "))

print(f"nombre completo del empleado: {nombre} {Apellidos} \nAntiguedad: {añoActual-ingreso} años")
