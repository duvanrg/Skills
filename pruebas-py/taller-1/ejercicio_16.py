"""
Crea un programa que solicite al usuario ingresar una serie de números positivos y luego calcule e imprima el promedio de los números ingresados utilizando un bucle while. El programa debe terminar cuando l usuario ingrese un número negativo.
"""
import os

os.system("clear")

numbers = []
invalido = 0
sumaNums = 0
serie = int(input("Ingrese el tamaño de la serie de numeros: "))

for i in range(0,serie):
    if (num := int(input("Ingrese el primer numero positivo: "))) >= 0:
        print(num)
        numbers.append(num)
    else:
        print(f"el numero {num} es un numero negativo")
        invalido = 1
        break

#print(f"el promedio de la serie de numeros es: \n {sum(numbers)/len(numbers)}")

if invalido != 1:
    while len(numbers) > 0:
        sumaNums += numbers.pop()

        if (len(numbers) == 0):
            print(f"el promedio de la serie de numeros es: \n {sumaNums/serie}")    
 
