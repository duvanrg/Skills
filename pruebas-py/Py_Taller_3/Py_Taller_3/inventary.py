import providers as supp
import shop 
import os

if __name__ == '__main__':
    inventary = {{'005': {'Codigo': 5, 'Nombre': 'Martillo', 'precio': 15000, 'stockActual': 0, 'stockMinimo': 15, 'stockMaximo': 50, 'Estado': 'No Disponible', 'proveedor': {}, 'Compras': {}, 'ventas': {}}}
}
    providers = {{'005': {'Codigo': 5, 'Nombre': 'Juan', 'direccion': 'Finca la herreria', 'telefono': 3052358712}}
}
    purchase = {}
    sold = {}
    isAddProduct = True
    opc = 0
    
    while isAddProduct:
        os.system("clear")
        print('+','-'*68,'+')
        print("|{:^70}|".format('FERRETERIA LA SOLDADA'))
        print('+','-'*68,'+')
        print("|{:^70}|".format('MENU'))
        print('+','-'*68,'+')
        print("1. Ingresar Producto","2. Listar Productos","3. Ingresar un proveedor","4. Listar Proovedores","5. Ingresar Compra","6. Listar compras","7. Ingresar Venta","8. Listar Ventas","9. Sair",sep=("\n"))
        try: 
            opc = int(input("> "))
            if (opc == 1):
                shop.AddProduct(inventary)
            elif (opc == 2):
                print(inventary)
            elif (opc == 3):
                supp.AddProvider(providers)
            elif (opc == 4):
                print(providers)    
            elif (opc == 5):
                shop.AddBuy(inventary, providers, purchase)
            elif (opc == 6):
                print(purchase)
            elif (opc == 7):
                shop.AddSell(inventary, providers, sold)
            elif (opc == 8):
                shop.AddSell(providers)
            elif (opc == 9):
                isAddProduct = False
                print("SALIENDO...")
        except Exception as e:
            print("Ocurrio un error: ",e)
        os.system("sleep 4")
        