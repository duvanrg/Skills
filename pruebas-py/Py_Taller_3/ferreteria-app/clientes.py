import core
import os


diccClientes = {'data': []}

def LoadInfoCliente(*args):
    global diccClientes
    if (core.checkFile(args)):
        return core.LoadInfo(args)
    else:
        core.crearInfo(args, diccClientes)
        return core.LoadInfo(args)


def MainMenu():
    os.system("clear")
    isCliRun = True
    diccCliente = LoadInfoCliente("clientes.json")
    print('+','-'*55,'+')
    print("|{:^57}|".format('ADMINISTRACION DE CLIENTES'))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar cliente")
    print("3. Editar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar menu principal")
    opcion =int(input("> "))
    if (opcion == 1):
        data = {
            "Id" : input("Ingrese el id del cliente: "),
            "Nombre" : input("Nombre del cliente: "),
            "Email" : input("Email del cliente: ")
        }
        core.crearInfo("clientes.json", data)
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
    
