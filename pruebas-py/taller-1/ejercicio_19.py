"""
En su casa le solicitan que realice un algoritmo en Python, que permita calcular el valor a pagar por concepto
de energía eléctrica. Los datos que se conocen son los siguientes:
- Mes de consumo
- Valor kw
- Total kw consumido en el mes
- estrato
"""
import os

os.system("cls")

desc = 1
valorNeto = 0

print("ingresa los datos correspondientes")
mes = input("mes: ")
valorKw = float(input("Valor kw: "))
consumo = float(input("consumido x mes: "))
estrato = int(input("estrato: "))

subTotal = valorKw * consumo

if (estrato == 1):
    desc = 0.6
    valorNeto = subTotal + subTotal * desc
elif (estrato == 2):
    desc = 0.5
    valorNeto = subTotal + subTotal * desc
elif (estrato == 3):
    desc = 0.15
    valorNeto = subTotal + subTotal * desc
else:
    valorNeto = subTotal


os.system("cls")

print("\n***Valor a pagar por concepto de energía eléctrica***")
print(f"Mes de consumo: {mes}")
print(f"Total de kilovatios consumidos: {consumo}")
print(f"Valor por kilovatio: ${valorKw}")
print(f"Estrato: {estrato}")
print(f"Subtotal: ${subTotal :.2f}")
print(f"Valor a pagar: ${valorNeto :.2f}")
