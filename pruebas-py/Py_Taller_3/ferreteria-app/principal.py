import os
import clientes
import compras
import ventas
import productos
import proveedores

if __name__ == "__main__":
    opc = 0
    isActivate = True
    dataproductos={'data':[]}
    dataproveedores={'data':[]}
    datacompras={'data':[]}
    dataventas={'data':[]}
    while isActivate:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format('MENU PRINCIPAL'))
        print('+','-'*55,'+')
        print("1. Gestion de clientes","2. Gestion de producto","3. Gestion de Proveedores","4. Gestion de Compras","5. Gestion de ventas","6. Terminar", sep="\n")
        opc = int(input("> "))
        if opc == 1:
            clientes.MainMenu()
        elif opc == 2:
            productos.MainMenu()
        elif opc == 3:
            proveedores.MainMenu()
        elif opc == 4:
            compras.MainMenu()
        elif opc == 5:
            ventas.MainMenu()
        elif opc == 6:
            isActivate = False
        else:
            print("Opcion no valida....")
        
        os.system("sleep 3")