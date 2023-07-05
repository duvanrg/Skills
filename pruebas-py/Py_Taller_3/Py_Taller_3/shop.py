import os
import random


def AddProduct(myStock):
    os.system("clear")
    cod = input("Ingrese el Codigo del producto: ")
    nombre = str(input("Ingrese el nombre del producto: "))
    precio = int(input("Ingrese precio del producto: "))
    stockMin = int(input("ingrese el valor minimo del Stock: "))
    stockMax = int(input("ingrese el valor maximo del Stock: "))
    
    product = {
        cod: {
            "Codigo": cod, 
            "Nombre": nombre, 
            "precio": precio,
            "stockActual": 0,
            "stockMinimo": stockMin,
            "stockMaximo": stockMax, 
            "Estado": "No Disponible", 
            "proveedor":{},
            "Compras":{},
            "ventas":{}
            }
        }
    
    myStock.update(product)
    print()
    print('+','-'*68,'+')
    print("|{:^70}|".format('PRODUCTO AGREGADO CORRECTAMENTE'))
    print('+','-'*68,'+')

def AddBuy(myStock, MyProvider):
    listProv = []
    os.system("clear")
    item = myStock.get(input("Ingrese el codigo del producto a comprar: "),-1)
    if item != -1:
        os.system("clear")

        cod = int(input("Ingrese el Codigo de la compra: "))
        valor = int(input("Ingrese valor de la compra:"))
        fecha = str(input("Ingrese la fecha de la compra (dd/mm/aa): "))
        cantidad = int(input("Ingrese la cantidad comprada: "))
        print("Seleccione el proveedor: ")
        for i, provi in enumerate(MyProvider):
            print(f'{i+1}. {provi["Nombre"]}')
            listProv.append(provi["Nombre"])
        proveedor = listProv[int(input(">  "))-1]

        compra = {"Codigo": cod, "Fecha": fecha, "Valor": valor, "Cantidad": cantidad, "Proveedor": proveedor}
        myStock[item]["stockActual"] += cantidad 
        myStock(item)["proveedor"].update(proveedor)
        myStock[item]["Compras"].update(compra)
        if myStock[item]["stockActual"] > myStock[item]["stockMinimo"]:
            myStock[item]["Estado"] = "Disponible"
    else:
        print("el producto no se encontro")

def AddSell(myStock, MyProvider):
    os.system("clear")
    buy = True
    registro = {}
    #Ingresar los datos de facturacion y del cliente (Nro factura venta, fecha venta, Nro Id del cliente, Nombre del cliente) y despues se registran todos los productos que este compro (Cod producto, Cantidad vendida, valor unitario)
    nroFact = int(input("Ingrese el numero de factura: "))
    fechaVenta = str(input("Ingrese la fecha de la venta (dd/mm/aa): "))
    nombre = str(input("Ingrese el nombre del cliente: "))
    idCliente = input("Ingrese el id del cliente:")
    while buy:
        cod = myStock.get(input("Ingrese el codigo del producto a vender: "),-1)
        if cod != -1 and myStock[cod]["estado"] == "Disponible":
            cantidad = int(input("Ingrese la cantidad vendida: "))
            valorUni =  myStock[cod]["precio"]
            venta = {cod : {"Codigo": cod, "Cantidad": cantidad, "ValorUnitario": valorUni}}
            registro.update(venta)
            myStock[cod]["stockActual"] -= cantidad
            if myStock[cod]["stockActual"] < myStock[cod]["stockMinimo"]:
                myStock[cod]["Estado"] = "No Disponible"

            myStock[cod]["ventas"].update({nroFact:venta})
        elif (myStock[cod]["estado"] == "No Disponible"):
            print("El producto no esta disponible")
        else :
            print("el producto no se encontro")
    
        
