import core
import os

diccProveedores = {"data": []}

def LoadInfoProveedor(*args):
    global diccProveedores
    if (core.checkFile(args[0])):
        return core.LoadInfo(args[0])
    else:
        core.crearInfo(args[0], diccProveedores)
        return core.LoadInfo(args[0])

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
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('BUSCADOR DE PROVEEDORES'))
        print('+','-'*55,'+')
        provSearch = input("Ingrese el codigo del proveedor a buscar: ")
        for i, item in enumerate(diccProveedores["data"]):
            if (provSearch in item["Id"]):
                print(f'Id Proveedor : {item["Id"]}')
                print(f'Nombre Proveedor : {item["Nombre"]}')
                print(f'Email Proveedor : {item["Email"]}')
    elif (opcion == 3):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('EDITOR DE PROVEEDORES'))
        print('+','-'*55,'+')
        provSearch = input("Ingrese el codigo del proveedor a Editar: ")
        for i, item in enumerate(diccProveedores["data"]):
            if (provSearch in item["Id"]):
                item["Nombre"] = input("Ingrese el nuevo nombre: ") or item["Nombre"]
                item["Email"] = input("Ingrese el nuevo email: ") or item["Email"]
                core.EditarData("proveedor.json", diccProveedores)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('ELIMINACION DE PROVEEDORES'))
        print('+','-'*55,'+')
        provSearch = input("Ingrese el codigo del proveedor a eliminar: ")
        for i, item in enumerate(diccProveedores["data"]):
            if (provSearch in item["Id"]):
                itemDel = diccProveedores["data"].pop(i)
                core.EditarData("proveedor.json", diccProveedores)
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()
    
