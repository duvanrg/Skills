import os
import clientes
import compras
import productos
import proveedores
import ventas 

if __name__ == "__main__":
    dataClientes = {'data':[]}
    dataCompras = {'data':[]}
    dataProductos = {'data':[]}
    dataProveedores = {'data':[]}
    dataVentas = {'data':[]}
    dicCli = {
        "code": "002",
        "name": "Duban Rodriguez"
    }
    clientes.CreateData("clientes.json",dataClientes,dicCli)