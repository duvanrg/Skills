import core
import os

diccVentas = {"data":[]}
diccProductos = {"data": []}

def LoadInfoVentas(*args):
    global diccVentas
    if (core.checkFile(args[0])):
        return core.LoadInfo(args[0])
    else:
        core.crearInfo(args[0], diccVentas)
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
    diccVentas = LoadInfoVentas("ventas.json")
    diccProductos = LoadInfoProductos("productos.json")

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
        buy = 1
        data = {
            "Cod" : input("Ingrese el Cod del venta: "),
            "Fecha" : input("Fecha de la venta: "),
            "IdCli" : input("Ingrese el Id del Cliente: "),
            "NombreCli" : input("Ingrese el nombre del Cliente: "),
            "Total" : 0,
            "DetalleVenta" : []
        }
        while buy == 1:
            cod = input("Ingrese el codigo del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            valorUni = int(input("Ingrese el valor por unidad del producto: "))
            venta = {"Codigo": cod, "Cantidad": cantidad, "ValorUnitario": valorUni}
            data["DetalleVenta"].append(venta)
            print("Desea vender otro producto \n1.Si \n2.No ")
            buy = int(input("> "))
        for i, item in enumerate(data["DetalleVenta"]):
            
            data["Total"] += item["Cantidad"] * item["ValorUnitario"]
        core.crearInfo("ventas.json", data)
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('BUSCADOR DE VENTAS'))
        print('+','-'*55,'+')
        ventaSearch = input("Ingrese el codigo del venta a buscar: ")
        for i, item in enumerate(diccVentas["data"]):
            if (ventaSearch in item["Cod"]):
                print(f'Codigo venta : {item["Cod"]}')
                print(f'Fecha venta : {item["Fecha"]}')
                print(f'ID Cliente : {item["IdCli"]}')
                print(f'Nombre Cliente : {item["NombreCli"]}')
                print("------------Productos------------")
            for vent in item["DetalleVenta"]:
                print(f'Codigo producto : {vent["Codigo"]}')
                print(f'Cantidad producto : {vent["Cantidad"]}')
                print(f'Valor unitario producto : {vent["ValorUnitario"]}')
            print(f'Total venta : {item["Total"]}')
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    os.system("sleep 5")    
    if (isCliRun):
        MainMenu()


