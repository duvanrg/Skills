"""
La FIFA desea crear un programa en Python que le permita llevar el registro y control de los equipos que van a participar en el mundial femenino sub 20 que se va a desarrollar en Colombia. El torneo 8888888888888888888cuenta con 16 equipos inscritos los cuales están organizados en 4 grupos y cada grupo se encuentra asignado a 4 diferentes ciudades de Colombia (Cali, Medellin, Bucaramanga y Bogota). 
Los equipos que participan en el torneo deben realizar el registro de los integrantes al momento de llegar al país, los datos que se deben registrar son los siguientes:
        
- Plantel de Jugadores 
    - Nombre, Nro dorsal, Posición de juego y edad.
- Plantel Técnico
    - Nombre, cargo, edad
- Plantel Medico
    - Nombre, especialidad y edad

La información suministrada anteriormente debe estar agrupada por país de representación. Cada equipo por país debe tener el nombre del país que representa y a que grupo pertenece.

El programa debe se permitir llevar el control de las diferentes estadísticas del torneo. La información estadística debe estar organizada de la siguiente forma:
        

El programa debe presentar el siguiente menú de opciones:
        

1. Registro de Equipo
1.1. Registro de Jugador(es) :
        Esta opción debe permitir ingresar uno o varios jugadores
según sea el caso (Uso while)
1.2. Registro Cuerpo técnico :
        tener en cuenta la observación del punto 1.1.
1.3. Registro Cuerpo medico :
        Tener en cuenta la observación del punto 1.1.
2. Registro de fecha :
        En esta opción el administrador del torneo podrá realizar el registro de cada uno de los Partidos jugados. El administrador deberá ingresar la fecha del juego, equipo local , equipo visitante y el marcador obtenido en el partido. El programa debe de forma automática identificar el equipo ganador y El equipo perdedor y así asignar sumar los partidos jugados, perdidos, empatados y ganados según Sea el caso.
3. Mostrar tabla de estadísticas :
        Esta opción el usuario deberá ingresar el grupo a consultar y el programa Mostrara la siguiente información.

4. Consultar información por equipo :
        Esta opción permitirá buscar información de un equipo Equipo especifico. El usuario deberá ingresar el nombre del equipo a consultar.

5. Mostrar equipos clasificados a 8vos:
        Esta opción permitirá mostrar los 8 equipo clasificados a octavos. Los equipos que pasan a octavos son los dos primeros equipos con mayor puntaje.

6. Mostrar el listado de jugadores de un equipo :
        Esta opción permitirá listar los jugadores que se encuentran Registrados en un equipo especifico.
7. Equipo que mayor cantidad de goles marco por cada grupo. El programa mostrara por cada grupo el nombre del equipo que mas goles marco en cada grupo.

Nota. Cada partido ganado otorga 3ptos al equipo ganador, 1 pto en caso de empate, recuerde que el total De puntos de cada equipo se obtiene a partir de los partidos ganados y empatados.
"""

import os

os.system("cls")

opc = 0
sub20 = []
partidos = []
grupos = [["Grupo A", "Cali",0],["Grupo B", "Medellin", 0],["Grupo C","Bucaramanga", 0],["Grupo D", "Bogota", 0]]

os.system("color a")


x = True
while x:
    y = False
    print("-------MUNDIAL SUB 20-----")
    print("1. Equipos","2. Registro de fecha","3. Tabla de estadísticas","4. Consultar información por equipo","5. Equipos clasificados a 8vos","6. Listado de jugadores","7. Equipo con mas goles por grupo","8. Salir",sep="\n")
    opc = int(input("Digite una opcion: "))

    if (opc == 1):
        y = True
        while y:
            os.system("cls")
            print("-------MENU EQUIPOS-----")
            print("1. Registro equipos","2. Registro Jugadores","3. Registro cuerpo tecnico","4. Registro cuerpo medico","5. Salir", sep="\n")
            opc = int(input("Digite una opcion: "))

            if (opc == 1):
                os.system("cls")

                print("-------REGISTRO DE EQUIPO-----")
                nombreEq = str(input("Nombre del equipo: "))
                for i, lista in enumerate(grupos):
                    if lista[2] != 4:
                        grupo = lista[0]
                        lista[2] += 1
                        break
                equipo = [nombreEq, grupo, [], [], [], [0,0,0,0,0,0,0]]
                sub20.append(equipo)         
            elif (opc == 2):
                os.system("cls")

                if (len(sub20) > 0):    
                    print("-------REGISTRO DE JUGADORES -----")
                    cont = 1
                    print("Lista de equipos")
                    for i in sub20:
                        print(f"{cont}. {i[0]}")
                        cont += 1
                    equipo = int(input("\nSeleccione el numero del equipo:"))-1

                    os.system("cls")
                    point = sub20[equipo][0]
                    print(f"-------REGISTRO DE JUGADORES ({point}) -----")
                    print(f"Cuantos jugadores va a ingresar? ")
                    jgd = int(input())
                    while (jgd > 0):
                        print("ingrese los datos del Jugador")
                        nombre = str(input("Nombre: "))
                        dorsal = int(input("numero de dorsal: ")) 
                        posición = str(input("Posicion de juego: ")) 
                        edad = int(input("Edad: "))
                        jugador = [nombre, dorsal, posición, edad]
                        sub20[equipo][2].append(jugador)
                        jgd -= 1
                else:
                    print("Aun no hay equipos registrados")
            elif (opc == 3):
                os.system("cls")
                if (len(sub20) > 0):
                    print("-------REGISTRO DEL CUERPO TECNICO-----")
                    cont = 1
                    print("Lista de equipos")
                    for i in sub20:
                        print(f"{cont}. {i[0]}")
                        cont += 1
                    equipo = int(input("\nSeleccione el numero del equipo:"))-1

                    os.system("cls")
                    point = sub20[equipo][0]
                    print(f"-------REGISTRO DEL CUERPO TECNICO ({point}) -----")
                    print(f"Cuantas personas va a ingresar? ")
                    cT = int(input())
                    while (cT > 0):
                        print("ingrese los datos la persona del cuerpo tecnico")
                        nombre = str(input("Nombre: "))
                        cargo = str(input("Cargo: ")) 
                        edad = int(input("Edad: "))
                        cuerpoT = [nombre, cargo, edad]
                        sub20[equipo][3].append(cuerpoT)
                        cT -= 1
                else:
                    print("Aun no hay equipos registrados")
            elif (opc == 4):
                os.system("cls")
                if (len(sub20) > 0):
                    print("-------REGISTRO DEL CUERPO MEDICO-----")
                    cont = 1
                    print("Lista de equipos")
                    for i in sub20:
                        print(f"{cont}. {i[0]}")
                        cont += 1
                    equipo = int(input("\nSeleccione el numero del equipo:"))-1

                    os.system("cls")
                    point = sub20[equipo][0]
                    print(f"-------REGISTRO DEL CUERPO MEDICO ({point}) -----")
                    print(f"Cuantas personas va a ingresar? ")
                    cM = int(input(""))
                    while (cM > 0):
                        print("ingrese los datos la persona del cuerpo medico")
                        nombre = str(input("Nombre: "))
                        esp = str(input("Especialidad: ")) 
                        edad = int(input("Edad: "))
                        cuerpoT = [nombre, esp, edad]
                        sub20[equipo][4].append(cuerpoT)
                        cT -= 1
                else:
                    print("Aun no hay equipos registrados")
            elif (opc == 5):
                os.system("cls")
                break
            else:
                print("Seleccion incorrecta")
            os.system("PAUSE")

    elif (opc == 2):
        if (len(sub20) >= 2):
            cont1 = 1
            cont2 = 1
            selectLocal = []
            selectVisitante = []
            resultado = ""
            os.system("cls")
            print("-------REGISTRO DEL PARTIDO-----")
            print("Ingrese los datos del partido")
            fecha = input("Fecha del juego (dd/mm/aa): ")
            print("Eliga el equipo Local:")
            for i in sub20:
                print(f"{cont1}. {i[0]}")
                cont1 += 1
                selectLocal.append(i)
            local = selectLocal[int(input("Seleccionalo: "))-1]
            print(f"Eliga el equipo visitante del {sub20[local][1]}:")
            for i in sub20:
                if (i[1] == sub20[local][1]):
                    if (i[local-1] != i[0]):
                        print(f"{cont1}. {i[0]}")
                        cont1 += 1
                        selectVisitante.append(i)
            visitante = selectVisitante[int(input("Seleccionalo: "))-1]
            golLocal = int(input("Goles del equipo local: "))
            golVisitante = int(input("Goles del equipo visitante: "))
            os.system("cls")
            print("-------RESULTADOS-----")
            resultado = f"{local[0]} [{golLocal}] - [{golVisitante}] {visitante[0]}"
            print(resultado)
            if (golLocal > golVisitante):
                print(f"Ganador : {local[0]}")
                print(f"Perdedor : {visitante[0]}")
                sub20[sub20.index(local)][6][1] += 1
                sub20[sub20.index(local)][6][6] += 3

                sub20[sub20.index(visitante)][6][3] += 1
            elif (golLocal < golVisitante):
                print(f"Ganador : {visitante[0]}")
                print(f"Perdedor : {local[0]}")
                sub20[sub20.index(visitante)][6][1] += 1
                sub20[sub20.index(visitante)][6][6] += 3

                sub20[sub20.index(local)][6][3] += 1
            elif (golLocal == golVisitante):
                print("Empate")            
                sub20[sub20.index(local)][6][2] += 1
                sub20[sub20.index(local)][6][6] += 1
                sub20[sub20.index(visitante)][6][2] += 1
                sub20[sub20.index(visitante)][6][6] += 1

            sub20[sub20.index(local)][6][0] += 1
            sub20[sub20.index(local)][6][4] += golLocal
            sub20[sub20.index(local)][6][5] += golVisitante
            sub20[sub20.index(visitante)][6][0] += 1
            sub20[sub20.index(visitante)][6][4] += golVisitante
            sub20[sub20.index(visitante)][6][5] += golLocal

            save = [fecha, local, visitante, golLocal, golVisitante, resultado]
            print(f"Equipos local: \n {sub20[sub20.index(local)]}")
            print(f"Equipos Visitante: \n {sub20[sub20.index(visitante)]}")
            partidos.append(save)
            os.system("PAUSE")

        else:
            print("deben haber como minimo 2 equipos diferentes para hacer un partido")
    
    elif (opc == 3):
        os.system("cls")
        if (len(sub20) > 0):
            print("-------TABLAS ESTADISTICAS-----")
            print("seleccione el grupo:")
            for i, group in enumerate(grupos):
                print(f"{i+1}. {group[0]}")
            select = grupos[int(input("digite su eleccion:"))-1]
            print('+', '-'*66, '+') 
            print("|{:^30}{}{:^31}|".format(' ',select[0],' '))
            print('+', '-' *66, '+')
            for j in sub20:
                if (j[1] == select[0]):
                    print(f'''| {j[0]:^18}|{j[2]:^6}|{j[3]:^6}|{j[4]:^6}|{j[5]:^6}|{j[6]:^6}|{j[7]:^6}|{j[8]:^6}|''')
                    print('+', '-' *66, '+')
        else:
            print("Aun no hay equipos registrados")
    
    elif (opc == 4):
        os.system("cls")
        if (len(sub20) > 0):
            print("-------CONSULTAR EQUIPO------")
            print("selecciona el equipo:")
            for i in sub20:
                print(f"{cont}. {i[0]}")
                cont += 1
            equipo = int(input("\nSeleccione el numero del equipo:"))-1

            print('+', '-'*66, '+') 
            print("|{:^30}{}{:^31}|".format(' ',sub20[equipo][0],' '))
            print('+', '-' *66, '+')
            for j in sub20:
                if (sub20[j] == sub20[equipo]):
                    print(f'''| {j[1]:^18}|{j[2]:^6}|{j[3]:^6}|{j[4]:^6}|{j[5]:^6}|{j[6]:^6}|{j[7]:^6}|{j[8]:^6}|''')
                    print('+', '-' *66, '+')
            
        else:
            print("Aun no hay equipos registrados")
    elif (opc == 5):
        os.system("cls")
        if (len(sub20) > 0):
            octavos = []
            grp = 1
            print("-------OCTAVOS DE FINAL------")
            while grp <=4 :
                for j in grupos:
                    mayor1 = 0
                    mayor2 = 0
                    for i in sub20:
                        if i[1] == j[0]:
                            if i[6][6] >mayor1:
                                grupo = j[0]
                                mayor1= i[6][6]
                    octavos.append([grupo, mayor1, mayor2])
            print("octavos de final:")
            for octa in octavos:
                print(octa)
        else:
            print("Aun no hay equipos registrados")
    elif (opc == 6):
        os.system("cls")
        if (len(sub20) > 0):
            print("-------LISTAR JUGADORES ------")
            cont = 1
            print("Lista de equipos")
            for i in sub20:
                print(f"{cont}. {i[0]}")
                cont += 1
            equipo = int(input("\nSeleccione el numero del equipo:"))-1

            print('+', '-'*66, '+') 
            for jgd in sub20[equipo][2]:
                print(f'''| {jgd[0]:^12}|{jgd[1]:^12}|{jgd[2]:^12}|{jgd[3]:^12}|''')
                print('+', '-' *66, '+')

            os.system("cls")
        else:
            print("Aun no hay equipos registrados")
    elif (opc == 7):
        os.system("cls")
        if (len(sub20) > 0):
            mayorGrupo = []
            grp = 1
            print("-------OCTAVOS DE FINAL------")
            while grp <=4 :
                for j in grupos:
                    mayor1 = 0
                    for i in sub20:
                        if i[1] == j[0]:
                            if i[6][4] >mayor1:
                                grupo = j[0]
                                mayor1= i[6][4]
                    mayorGrupo.append([grupo, mayor1])
            print("octavos de final:")
            for goles in mayorGrupo:
                print(goles)
        else:
            print("Aun no hay equipos registrados")
    elif (opc == 8):
        x = False

    else:
        print("Opcion invalida")
    os.system("PAUSE")



