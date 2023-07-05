"""
Campus requiere administrar algunos datos de sus Campers como por ejemplo, la creación, eliminación o búsqueda de los developers, entre otros, por tal razón, ha solicitado el diseño de un programa que cuente con el siguiente menú como panel de control:C
"""
import os

os.system("clear")
grpSpnt = 0
grpArtm = 0
artm = []
spnt = []
x = True
campersArtm = []
campersSpnt = []
busc = 0



while x == True:
    y = False
    print("---------------------MENU---------------------")
    print("1. GRUPO ARTEMIS:", "2. GRUPO SPUTNIK", "3. SALIR", sep="\n")
    opc = input("Digite Una Opcion: ")
    if opc == "1":
        os.system("clear")
        print("°°°°°°°°°°°°°°°°GRUPO ARTEMIS°°°°°°°°°°°°°°°°")
        cont = 0
        if (len(artm) == 0):
            select = str(input("No existe ningun grupo de Artemis \nDesea crear uno (S/N)"))
            if select.upper() == "S":
                opc = "1"
            else:
                opc = "3"
        else: 
            print(f"1. CREAR UN NUEVO GRUPO","2. SELECCIONAR GRUPO","3. SALIR",sep=("\n"))
            opc = input("Digite Una Opcion: ")

        if (opc == "1"):    
            os.system("clear")    
            print("°°°°°°°°°°°°°°°°CREAR GRUPO ARTEMIS°°°°°°°°°°°°°°°°")
            group = input("ingrese el nombre para el grupo artemis \ndebe tener una letra mayuscula y un digito: ")
            if (group in artm):
                print(f"El Grupo {group} ya existe")
                break            
            artm.append(group)
            artm.append([])
        elif (opc == "2"):
            print("Seleccione el grupo")
            for i, grp in enumerate(artm):
                if i%2 ==0:
                    cont += 1
                    print(f"{cont}. {grp}")
            select = input()
            y = True
        elif (opc == "3"):
            print("Saliendo...")
            os.system("sleep 2")
            break
        else:
            os.system("clear")
            print("⚠️⚠️⚠️ Opción inválida ⚠️⚠️⚠️")
            os.system("sleep 2")

        while (y == True):
            ubi = artm[(int(select)-1)*2]
            os.system("clear")
            print(f"°°°°°°°°°°°°°°°°GRUPO ARTEMIS: {ubi}°°°°°°°°°°°°°°°°")
            print("1. LISTAR CAMPERS DE ARTEMIS", "2. AGREGAR CAMPERS A ARTEMIS", "3. ELIMINAR CAMPERS DE ARTEMIS", "4. ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS", "5. BUSCAR CAMPER EN LISTA DE ARTEMIS","6.SALIR", sep="\n")
            opc = input("Digite Una Opcion: ")

            if opc == "1":
                os.system("clear")
                print(f"~~~~~~~~~~~~~LISTAR CAMPERS DE ARTEMIS {ubi}~~~~~~~~~~~~~")
                if (len(campersArtm) > 0):
                    for i, lista in enumerate(campersArtm):
                        if (ubi in lista):
                            print(lista)
                else:
                    print(f"No Existe ningun camper registrado en el grupo {ubi}")
                    
            elif opc == "2":
                os.system("clear")
                print(F"~~~~~~~~~~~~~AGREGAR CAMPERS A ARTEMIS {ubi} ~~~~~~~~~~~~~")
                print("Ingrese los datos del camper")
                nombre = str(input("Nombre: "))
                apellidos = str(input("Apellidos: "))
                doc = int(input("Documento: "))
                tipoDoc = str(input("Tipo Documento (CC/TI/DNI/CI): "))
                edad = int(input("Edad: "))
                celular= str(input("Celular: "))
                jornada = str(input("Jornada (Mañana/Tarde): "))
                grupo = ubi
                calificaciones = []
                """
                if (codigo in campersArtm[0]):
                    print("el codigo Asignado ya existe")
                """
                camper = [nombre, apellidos, doc, tipoDoc, edad, celular, jornada, grupo, calificaciones]
                campersArtm.append(camper)
                artm[(int(select)*2)-1].append(camper)

                print("✅✅✅ Camper agregado correctamente ✅✅✅ \nSaliendo al menu")

            elif opc == "3":
                os.system("clear")
                print(f"~~~~~~~~~~~~~ELIMINAR CAMPERS DE ARTEMIS {ubi}~~~~~~~~~~~~~")
                encontrado = False
                print("Ingrese el documento del camper que desea eliminar")
                busc = int(input())
                for cmp in campersArtm:
                    if (busc in cmp):
                        if (ubi in cmp):
                            campersArtm.remove(cmp)
                            encontrado = True
                            break

                if encontrado:
                    print("✅✅✅ Camper eliminado correctamente ✅✅✅")
                    os.system("sleep 2")
                else:
                    print("❌❌❌ No se encontró el documento en la lista ❌❌❌")

                        
            elif opc == "4":
                os.system("clear")
                print(f"~~~~~~~~~~~~~ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS {ubi}~~~~~~~~~~~~~")
                if (len(campersArtm) > 0):
                    campersArtm.sort(key=lambda x: x[1])
                    for i, lista in enumerate(campersArtm):
                        print(lista)
                else:
                    print(f"No Existe ningun camper registrado en el grupo {ubi}")
                
            elif opc == "5":
                os.system("clear")
                print(f"~~~~~~~~~~~~~BUSCAR CAMPER EN LISTA DE ARTEMIS {ubi}~~~~~~~~~~~~~")
                encontrado = False
                print("Ingrese el documento del camper que desea buscar: ")
                busc = input()
                for cmp in campersArtm:
                    if (busc in cmp):
                        if (ubi in cmp):
                            print(cmp)
                            encontrado = True
                            break

                if encontrado:
                    print("✅✅✅ Camper encontrado correctamente ✅✅✅")
                    os.system("sleep 2")
                else:
                    print("❌❌❌ No se encontró el documento en la lista ❌❌❌")
            elif (opc == "6"):
                print("Saliendo...")
                os.system("sleep 2")
                break
            else:
                os.system("clear")
                print("⚠️⚠️⚠️ Opción inválida ⚠️⚠️⚠️")
            os.system("sleep 2")

    elif opc == "2":
        os.system("clear")
        print("°°°°°°°°°°°°°°°°CREAR GRUPO SPUTNIK°°°°°°°°°°°°°°°°")

        if (len(spnt) == 0):
            select = str(input("No existe ningun grupo de sputnik \nDesea crear uno (S/N): "))
            if select.upper() == "S":
                opc = "1"
            else:
                opc = "3"
        else: 
            print(f"1. CREAR UN NUEVO GRUPO","2. SELECCIONAR GRUPO","3. SALIR",sep=("\n"))
            opc = input("Digite Una Opcion: ")


        if (opc == "1"):    
            os.system("clear")  
            cont = 0  
            print("°°°°°°°°°°°°°°°°CREAR GRUPO SPUTNIK°°°°°°°°°°°°°°°°")
            group = input("ingrese el nombre para el grupo sputnik \ndebe tener una letra mayuscula y un digito: ").upper()
            if (group in spnt):
                print(f"El Grupo {group} ya existe")
                break
            spnt.append(group)
            spnt.append([])
        elif (opc == "2"):
            print("Seleccione el grupo")
            for i, grp in enumerate(spnt):
                cont += 1
                print(f"{cont}. {grp}")
            select = input()
        elif (opc == "3"):
            print("Saliendo...")
            os.system("sleep 2")
            break
        else:
            os.system("clear")
            print("⚠️⚠️⚠️ Opción inválida ⚠️⚠️⚠️")
            os.system("sleep 2")
        
        while (y == True):
            ubi = spnt[(int(select)-1)*2]
            os.system("clear")
            print(f"°°°°°°°°°°°°°°°°GRUPO SPUTNIK: {ubi}°°°°°°°°°°°°°°°°")
            print("1. LISTAR CAMPERS DE SPUTNIK", "2. AGREGAR CAMPERS A SPUTNIK", "3. ELIMINAR CAMPERS DE SPUTNIK", "4. ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK", "5. BUSCAR CAMPER EN LISTA DE SPUTNIK","6. SALIR", sep="\n")
            opc = input("Digite Una Opcion: ")

            if opc == "1":
                os.system("clear")
                print(f"~~~~~~~~~~~~~LISTAR CAMPERS DE SPUTNIK {ubi}~~~~~~~~~~~~~")
                if (len(campersSpnt) > 0):
                    for i, lista in enumerate(campersSpnt):
                        if (ubi in lista):
                            print(lista)
                else:
                    print(f"No Existe ningun camper registrado en el grupo {ubi}")
                    
                input("Precione Enter para continuar")
                
            elif opc == "2":
                os.system("clear")
                print(f"~~~~~~~~~~~~~AGREGAR CAMPERS A SPUTNIK {ubi}~~~~~~~~~~~~~")
                print("Ingrese los datos del camper")
                nombre = str(input("Nombre: "))
                apellidos = str(input("Apellidos: "))
                doc = int(input("Documento: "))
                tipoDoc = str(input("Tipo Documento (CC/TI/DNI/CI): "))
                edad = int(input("Edad: "))
                celular= str(input("Celular: "))
                jornada = str(input("Jornada (Mañana/Tarde): "))
                grupo = ubi
                calificaciones = []
                """
                if (codigo in campersSpnt[0]):
                    print("el codigo Asignado ya existe")
                """
                camper = [nombre, apellidos, doc, tipoDoc, edad, celular, jornada, grupo, calificaciones]
                campersSpnt.append(camper)
                spnt[(int(select)*2)-1].append(camper)

                print("✅✅✅ Camper agregado correctamente ✅✅✅ \nSaliendo al menu")
                
            elif opc == "3":
                os.system("clear")
                print(f"~~~~~~~~~~~~~ELIMINAR CAMPERS DE SPUTNIK {ubi}~~~~~~~~~~~~~")
                encontrado = False
                print("Ingrese el documento del camper que desea eliminar")
                busc = int(input())
                for cmp in campersSpnt:
                    if (busc in cmp):
                        if (ubi in cmp):
                            campersSpnt.remove(cmp)
                            encontrado = True
                            break

                if encontrado:
                    print("✅✅✅ Camper eliminado correctamente ✅✅✅")
                    os.system("sleep 2")
                else:
                    print("❌❌❌ No se encontró el documento en la lista ❌❌❌")
                        
            elif opc == "4":
                os.system("clear")
                print(f"~~~~~~~~~~~~~ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK {ubi}~~~~~~~~~~~~~")
                if (len(campersSpnt) > 0):
                    campersSpnt.sort(key=lambda x: x[1])
                    for i, lista in enumerate(campersSpnt):
                        print(lista)
                else:
                    print(f"No Existe ningun camper registrado en el grupo {ubi}")
                
            elif opc == "5":
                os.system("clear")
                print(f"~~~~~~~~~~~~~BUSCAR CAMPER EN LISTA DE SPUTNIK {ubi}~~~~~~~~~~~~~")
                encontrado = True
                print("Ingrese el documento del camper que desea buscar: ")
                busc = input()
                for cmp in campersSpnt:
                    if (cmp == busc):
                        if (ubi in cmp):
                            print(cmp)
                            encontrado = True
                            break

                if encontrado:
                    print("✅✅✅ Camper encontrado correctamente ✅✅✅")
                    os.system("sleep 2")
                else:
                    print("❌❌❌ No se encontró el documento en la lista ❌❌❌")
            elif (opc == "6"):
                print("Saliendo...")
                os.system("sleep 2")
                break
            else:
                os.system("clear")
                print("⚠️⚠️⚠️ Opción inválida ⚠️⚠️⚠️")
            os.system("sleep 2")

    elif (opc == "3"):
        print("Saliendo...")
        os.system("sleep 2")
        break
    else:
        os.system("clear")
        print("⚠️⚠️⚠️ Opción inválida ⚠️⚠️⚠️")
        os.system("sleep 2")




