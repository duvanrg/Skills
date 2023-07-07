import core
import os

def LoadInfoVentas(*args):
    return core.LoadInfo("ventas.json")

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^57}|".format('ADMINISTRACION DE VENTAS'))
    print('+','-'*55,'+')

    print("1. Registrar venta")
    print("2. Buscar venta")
    print("3. Devolucion venta")
    print("4. Anular Factura de venta")
    print("5. Regresar menu principal")
    opcion =int(input("> "))
    if (opcion == 1):
        data = {
            "Id" : input("Ingrese el id del venta: "),
            "Nombre" : input("Nombre del venta: "),
            "Precio" : input("precio de la venta: ")
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


