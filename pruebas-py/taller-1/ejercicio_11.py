"""
Escribe un programa que solicite al usuario ingresar el nombre de un mes y determine cuántos días tiene ese mes. Utiliza estructuras condicionales para asociar cada mes con la cantidad correspondiente de días y muestra un mensaje con el resultado.
"""
import os

os.system("clear")

ind = 0
meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
mes = str(input("Ingrese el nombre de un mes: "))

if mes.lower() in meses:
    ind = meses.index(mes.lower())
    if ind+1 in [1,3,5,7,8,10,12]:
        print(f"el mes de {mes} tiene 31 dias")
    if ind+1 in [4,6,9,11]:
        print(f"el mes de {mes} tiene 30 dias")
    if ind+1 == 2:
        bis = str(input("el año es bisiesto si o no: "))
        if bis.lower() == "si":
            print(f"el mes de {mes} tiene 29 dias")
        else:
            print(f"el mes de {mes} tiene 28 dias")
else:
    print("el mes que ingreso no se encuentra")



