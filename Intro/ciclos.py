import os
mensaje = "hoy hace frio"
vocales = ['a','e','i','o','u']
contVoc = 0 #contador de las vocales 
contConso = 0 #contador de las consonates

# os.system('cls')
for i in range(1,5,2): # el step indica la los saltos entre el rango
    print(i)

for letra in mensaje:
    print(letra)

for letra in mensaje:
    if letra in vocales:
        contVoc +=1 #en cada iteracion se le suma +1 a la variable contVoc
    else:
        contConso +=1 #en cada iteracion se le suma +1 a la variable contCons

    print(f"[{letra}]", end="") #el end vacio elimina el salto de linea

print("\n")
# os.system('cls')
print(f"Total de vocales encontradas : {contVoc}")
print(f"Total de consontantes encontradas : {contConso}")
# os.system('pause')

# Ciclo while
# os.system('cls')

print("Ejemplo uso del ciclo while")
isAddItem = True
opc = 0
while (isAddItem):
    print("1. Agregar item","2. Buscar Item","3. Salir",sep="\n")
    opc = int(input(":)"))
    if (opc == 1):
        print("OK 1")
        
    elif (opc == 2):
        print("OK 2")
    elif (opc == 3):
        print("OK Chaoo")
        isAddItem = False
    else:
        print("Error")
    # os.system('pause')

# os.system('pause')
