import os

d1 = {
    "Nombre": "Camilo",
    "Edad": 22,
    "Documento": 1005,
    "Direccion": {
        "Ciudad": "Bogotá",
        "Barrio": {
            "Nombre": "Barrio 1",
            "Estrato": 2
        },
        "Nomenclatura": "hola y adios"
    }
}
d2 = {
    "Nomvbre": "Camilo",
    "Edad": 22,
    "Documento": 1005,
    "Emails": "camilo@gmail.com" 
}

ubicacion = {
    "Direccion": {
        "Ciudad": "Bogotá",
        "Barrio": {
            "Nombre": "Barrio 1",
            "Estrato": 2
        },
        "Nomenclatura": "hola y adios"
    }
}

print(d1)
d1["Direccion"]["Barrio"]["Estrato"]  =  6
print(d1)
#d1.pop("Direccion")
print(d1)
d1.update(d2)
print(d1)
os.system("clear")
print(d2)
d2.update(ubicacion)
print(d2)
os.system("clear")
for i in d1:
    print(i)

