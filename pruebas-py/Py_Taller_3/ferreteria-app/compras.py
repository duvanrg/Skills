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
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()
    
