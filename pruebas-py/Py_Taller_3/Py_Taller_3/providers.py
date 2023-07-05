import os

def AddProvider(myProvider):
    os.system("clear")
    cod = input("Ingrese el Codigo del Proveedor: ")
    nombre = str(input("Ingrese el nombre del Proveedor: "))
    direccion = str(input("Ingrese la direccion del Proveedor: "))
    telefono = int(input("Ingrese el telefono del Proveedor: "))
    
    provider = {
        cod: {
            "Codigo": cod, 
            "Nombre": nombre, 
            "direccion": direccion,
            "telefono": telefono, 
            }
        }
    
    myProvider.update(provider)

    print()
    print('+','-'*68,'+')
    print("|{:^70}|".format('PROOVEDOR AGREGADO CORRECTAMENTE'))
    print('+','-'*68,'+')