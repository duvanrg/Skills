import core
import os

diccProveedores = {"data": []}

def LoadInfoProveedor(*args):
    global diccProveedores
    if (core.checkFile(args)):
        return core.LoadInfo(args)
    else:
        core.crearInfo(args, diccProveedores)
        return core.LoadInfo(args)

def MainMenu():
    os.system("clear")
    isCliRun = True
    diccProveedores = LoadInfoProveedor("proveedores.json")
    print('+','-'*55,'+')
    print("|{:^57}|".format('ADMINISTRACION DE PROVEEDORES'))
    print('+','-'*55,'+')

    print("1. Registrar proveedor")
    print("2. Buscar proveedor")
    print("3. Editar proveedor")
    print("4. Eliminar proveedor")
    print("5. Regresar menu principal")
    opcion =int(input("> "))
    if (opcion == 1):
        data = {
            "Id" : input("Ingrese el id del proveedor: "),
            "Nombre" : input("Nombre del proveedor: "),
            "Email" : input("Email del proveedor: ")
        }
        core.crearInfo("proveedores.json", data)
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
    
