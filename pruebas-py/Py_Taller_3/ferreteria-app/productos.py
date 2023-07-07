import core
import os

diccProductos = {"data": []}

def CreateData(*args):
    global diccProductos
    if (core.checkFile(args[0])):
        return core.LoadInfo(args[0])
    else:
        core.crearInfo(args[0], diccProductos)
        return core.LoadInfo(args[0])

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
            "Precio" : input("precio unitario del producto: "),
            "StockMin" : input("stock Minimo del producto: "),
            "StockMax" : input("stock Maximo del producto: ")
        }
        core.crearInfo("productos.json", data)
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('BUSCADOR DE PRODUCTOS'))
        print('+','-'*55,'+')
        prodSearch = input("Ingrese el codigo del producto a buscar: ")
        for i, item in enumerate(diccProductos["data"]):
            if (prodSearch in item["Id"]):
                print(f'Id producto : {item["Id"]}')
                print(f'Nombre producto : {item["Nombre"]}')
                print(f'Precio producto : {item["Precio"]}')
                print(f'Stock minimo producto : {item["StockMin"]}')
                print(f'Stock maximo producto : {item["StockMax"]}')
    elif (opcion == 3):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('EDITOR DE PRODUCTOS'))
        print('+','-'*55,'+')
        prodSearch = input("Ingrese el codigo del producto a Editar: ")
        for i, item in enumerate(diccProductos["data"]):
            if (prodSearch in item["Id"]):
                item["Nombre"] = input("Ingrese el nuevo nombre: ") or item["Nombre"]
                item["Precio"] = input("Ingrese el nuevo precio: ") or item["Precio"]
                item["StockMin"] = input("Ingrese el nuevo Stock minimo: ") or item["StockMin"]
                item["StockMax"] = input("Ingrese el nuevo Stock maximo: ") or item["StockMax"]
                core.EditarData("productos.json", diccProductos)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('ELIMINACION DE PRODUCTOS'))
        print('+','-'*55,'+')
        prodSearch = input("Ingrese el codigo del producto a eliminar: ")
        for i, item in enumerate(diccProductos["data"]):
            if (prodSearch in item["Id"]):
                itemDel = diccProductos["data"].pop(i)
                core.EditarData("productos.json", diccProductos)
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()
    
