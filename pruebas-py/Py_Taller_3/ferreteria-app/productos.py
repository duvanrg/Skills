import core
import os

diccProductos = {"data": []}

def CreateData(*args):
    global diccProductos
    if (core.checkFile(args)):
        return core.LoadInfo(args)
    else:
        core.crearInfo(args, diccProductos)
        return core.LoadInfo(args)

def MainMenu():
    os.system("clear")
    isCliRun = True
    diccProductos = CreateData("productos.json")
    print('+','-'*55,'+')
    print("|{:^57}|".format('ADMINISTRACION DE PRODUCTOS'))
    print('+','-'*55,'+')

    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Editar producto")
    print("4. Eliminar producto")
    print("5. Regresar menu principal")
    opcion =int(input("> "))
    if (opcion == 1):
        data = {
            "Id" : input("Ingrese el id del producto: "),
            "Nombre" : input("Nombre del producto: "),
            "Precio" : input("precio unitario del producto: ")
        }
        core.crearInfo("productos.json", data)
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()
    
