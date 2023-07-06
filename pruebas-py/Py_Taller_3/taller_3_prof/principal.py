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
    compras.CreateData("compras.json",dataCompras)
    productos.CreateData("productos.json",dataProductos)
    proveedores.CreateData("proveedores.json",dataProveedores)
    ventas.CreateData("ventas.json",dataVentas)

    os.system("sleep 5")
    