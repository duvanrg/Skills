import core
import os

diccCompras = {"data": []}

def LoadDataCompras(*args):
    global diccCompras
    if (core.checkFile(args[0])):
        return core.LoadInfo(args[0])
    else:
        core.crearInfo(args[0], diccCompras)
        return core.LoadInfo(args[0])
    
def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    diccCompras = LoadDataCompras("compras.json")
    print('+','-'*55,'+')
    print("|{:^57}|".format('ADMINISTRACION DE COMPRAS'))
    print('+','-'*55,'+')

    print("1. Registrar")
    print("2. Buscar ")
    print("3. Devolucion")
    print("4. Anular Factura compra")
    print("5. Regresar menu principal")
    opcion =int(input("> "))
    if (opcion == 1):
        data = {
            "Id" : input("Ingrese el id del compra: "),
            "Nombre" : input("Nombre del compra: "),
            "Precio" : input("precio de la compra: ")
        }
        core.crearInfo("compras.json", data)
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('BUSCADOR DE CLIENTES'))
        print('+','-'*55,'+')
        compraSearch = input("Ingrese el codigo del cliente a buscar: ")
        for i, item in enumerate(diccCompras["data"]):
            if (compraSearch in item["Id"]):
                print(f'Id compra : {item["Id"]}')
                print(f'Nombre compra : {item["Nombre"]}')
                print(f'Precio compra : {item["Precio"]}')
    elif (opcion == 3):
        z
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()
    
