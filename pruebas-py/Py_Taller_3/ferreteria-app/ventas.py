import core
import os

def CreateData(*args):
    return core.LoadInfo("ventas.json")

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^57}|".format('ADMINISTRACION DE VENTAS'))
    print('+','-'*55,'+')

    print("1. Registrar")
    print("2. Buscar ")
    print("3. Devolucion")
    print("4. Anular Factura")
    print("5. Regresar menu principal")
    opcion =int(input("> "))
    if (opcion == 1):
        pass
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
    
