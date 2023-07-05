"""
Crea un programa que genere e imprima los primeros 50 números pares utilizando un bucle while.
"""
import os

os.system("clear")
cont = 1
num = 1

while (cont <=50):
    if (num%2 == 0):
        print(num)
        num +=2
    #print(cont*2) #otra forma de imprimir los numeros pares 
    cont += 1
    
