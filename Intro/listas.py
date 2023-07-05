import os
import time
ciudades = [] # Crear lista vacia

# Agregar elementos de la lista vacia  
ciudades.append("Bucaramanga")
ciudades.append("Cucuta")

# Imprimir lista
print(ciudades)

# Mostrar elemento de la lista
print(ciudades[0])

# Extender el contenido de la lista
municipios = ["Giron","Floridablanca","Ocaña"]
ciudades.extend(municipios)
print(ciudades)

# Insertar elementos de la lista
print(municipios)
municipios.insert(1, "Piedecuesta") # agrega la ciudad en la posicion index 1 y mueve los demas elementos 
# Municipios[1] = "Piedecuesta" # reemplaza el valor en la posicion index 1
print(municipios)


# Eliminar elementos de la lista
municipios = ["Giron","Floridablanca","Ocaña"]
municipios.remove("Floridablanca")

# Quitar el ultimo elemento de la lista
municipios = ["Giron","Floridablanca","Ocaña"]
deBaja = municipios.pop(2)
print(f"se elimino {deBaja} de la lista municipios")
print(municipios)

# sacar el index en el cual se encuentra un dato
municipios = ["Giron","Floridablanca","Ocaña"]
print(f'El elemento se encontro en la lista en la posicion {municipios.index("Giron")}')
print(municipios)

# Iterar elementos de la lista 
municipios = ["Giron","Floridablanca","Ocaña"]
for item in municipios:
    print(item)

for i, item in enumerate(municipios):
    print(f'El municipio {item} se encuentra en la posicion {i}')


