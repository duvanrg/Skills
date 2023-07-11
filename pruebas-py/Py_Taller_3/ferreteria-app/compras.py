import core
import os

diccCompras = {"data": []}
diccProductos = {"data": []}

def LoadInfoCompras(*args):
    global diccCompras
    if (core.checkFile(args[0])):
        return core.LoadInfo(args[0])
    else:
        core.crearInfo(args[0], diccCompras)
        return core.LoadInfo(args[0])

def LoadInfoProductos(*args):
    global diccProductos
    if (core.checkFile(args[0])):
        return core.LoadInfo(args[0])
    else:
        core.crearInfo(args[0], diccProductos)
        return core.LoadInfo(args[0])

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    diccCompras = LoadInfoCompras("compras.json")
    diccProductos = LoadInfoProductos("productos.json")
    print('+','-'*55,'+')
    print("|{:^57}|".format('ADMINISTRACION DE COMPRAS'))
    print('+','-'*55,'+')

    print("1. Registrar compra")
    print("2. Buscar compra")
    print("3. Devolucion compra")
    print("4. Anular Factura compra")
    print("5. Regresar menu principal")
    opcion =int(input("> "))
    if (opcion == 1):
        data = {
            "Cod" : input("Ingrese el Cod del compra: "),
            "Fecha" : input("Fecha de la compra: "),
            "CodProd" : input("Ingrese el Cod del Producto: "),
            "Valor" : input("Valor de la compra: "),
            "Cantidad" : input("Cantidad comprada: ")
        }
        core.crearInfo("compras.json", data)
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('BUSCADOR DE COMPRAS'))
        print('+','-'*55,'+')
        compraSearch = input("Ingrese el codigo del compra a buscar: ")
        for i, item in enumerate(diccCompras["data"]):
            if (compraSearch in item["Cod"]):
                print(f'Codigo compra : {item["Cod"]}')
                print(f'Fecha compra : {item["Fecha"]}')
                print(f'Valor compra : {item["Valor"]}')
                print(f'Cantidad compra : {item["Cantidad"]}')
    elif (opcion == 3):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('DEVOLUCION DE COMPRAS'))
        print('+','-'*55,'+')
        compraSearch = input("Ingrese el codigo del compra a devolver: ")
        for i, item in enumerate(diccCompras["data"]):
            if (compraSearch in item["Cod"]):
                diccCompras["data"][i]["Devolucion"] = True
                print(diccCompras["data"][i])
                core.EditarData("compras.json", diccCompras)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('ANULACION COMPRAS'))
        print('+','-'*55,'+')
        compraSearch = input("Ingrese el codigo del compra a devolver: ")
        for i, item in enumerate(diccCompras["data"]):
            if (compraSearch in item["Cod"]):
                diccCompras["data"][i]["Anulacion"] = True
                print(diccCompras["data"][i])
                core.EditarData("compras.json", diccCompras)
    elif (opcion == 5):
        isCliRun = False
    os.system("sleep 5")
    if (isCliRun):
        MainMenu()
    
