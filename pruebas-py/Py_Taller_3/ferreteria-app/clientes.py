import core
import os


diccClientes = {'data': []}

def LoadInfoCliente(*args):
    global diccClientes
    if (core.checkFile(args[0])):
        return core.LoadInfo(args[0])
    else:
        core.crearInfo(args[0], diccClientes)
        return core.LoadInfo(args[0])


def MainMenu():
    os.system("clear")
    isCliRun = True
    diccClientes = LoadInfoCliente("clientes.json")
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
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('BUSCADOR DE CLIENTES'))
        print('+','-'*55,'+')
        cliSearch = input("Ingrese el codigo del cliente a buscar: ")
        for i, item in enumerate(diccClientes["data"]):
            if (cliSearch in item["Id"]):
                print(f'Id Cliente : {item["Id"]}')
                print(f'Nombre Cliente : {item["Nombre"]}')
                print(f'Email Cliente : {item["Email"]}')
    elif (opcion == 3):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('EDITOR DE CLIENTES'))
        print('+','-'*55,'+')
        cliSearch = input("Ingrese el codigo del cliente a Editar: ")
        for i, item in enumerate(diccClientes["data"]):
            if (cliSearch in item["Id"]):
                item["Nombre"] = input("Ingrese el nuevo nombre: ") or item["Nombre"]
                item["Email"] = input("Ingrese el nuevo email: ") or item["Email"]
                core.EditarData("clientes.json", diccClientes)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('ELIMINACION DE CLIENTES'))
        print('+','-'*55,'+')
        cliSearch = input("Ingrese el codigo del cliente a eliminar: ")
        for i, item in enumerate(diccClientes["data"]):
            if (cliSearch in item["Id"]):
                itemDel = diccClientes["data"].pop(i)
                core.EditarData("clientes.json", diccClientes)
    elif (opcion == 5):
        isCliRun = False
    os.system('sleep 3')  
    if (isCliRun):
        MainMenu()
    
