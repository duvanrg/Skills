"""
Escribe un programa que solicite al usuario ingresar el día, el mes y el año de una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje indicando si la fecha es válida o no.
"""
import os

os.system("clear")

bisiesto = False
valido = 0

if (anyo := int(input("año: "))):
    if not anyo%4 and (anyo % 100 or not anyo % 400):
        bisiesto = True
if (mes := int(input("mes: "))) > 12 and valido == 0:
    print("mes invalido")
    valido == 1
if (dia := int(input("dia: "))) <= 31 and valido == 0:
    if (mes in [1,3,5,7,8,10,12]):
        pass
    if (mes in [4,6,9,11]):
        if dia  == 31:
            print("dia invalido por el mes")
            valido = 1
    if (mes == 2 and bisiesto == False):
        if dia >=29:
            print("dia invalido por el mes")
            valido = 1
    elif (mes == 2 and bisiesto == True):
        if dia >=30:
            print("dia invalido por el mes")
            valido = 1
else:
    print("dia invalido")
    valido == 1


if (valido == 0):
    print(f"la fecha: {dia}/{mes}/{anyo}")
else:
    print("la fecha fue invalidada")

