import os


def AddEquipo(equipos):
    os.system("clear")
    teamName = input("Ingrese el nombre del equipo: ").upper()
    myTeam = [teamName, [], [], [], [0,0,0,0,0,0,0]]
    #myTeam = {"Nombre": teamName,"Jugadores": [],"Tecnico": [],"Medico": [],"Datos": {"PJ":0,"PG":0,"PE":0,"PP":0,"GF":0,"GC":0,"PUNTOS":0}}
    
    equipos.append(myTeam)

def ShowEquipos(equipos):
    os.system("clear")
    print('+','-'*68,'+')
    print("|{:^25}{}{:^26}|".format(' ','LISTADO DE EQUIPOS ',' '))
    print('+','-'*68,'+')
    for equipo in equipos:
        print("|{:^70}|".format(equipo[0]))
        print('+','-'*68,'+')
        print("| {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^14} |".format('PJ','PG','PE','PP','GF','GC','PUNTOS'))
        print('+','-'*68,'+')
        print("| {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^14} |".format(equipo[4][0],equipo[4][1],equipo[4][2],equipo[4][3],equipo[4][4],equipo[4][5],equipo[4][6]))
        print('+','-'*68,'+')

def AddPlayer(equipos):
    isAddPlayer = True
    os.system("clear")
    equipo = input("ingrese el nombre del equipo: ").upper()
    for item in equipos:
        if equipo in item:
            while isAddPlayer:
                os.system("clear")
                posiciones = ["Arquero", "Defensa","Delantero","Medio Central"]
                nombrePlayer = input("Ingrese el nombre del Player: ")
                edadPlayer = input("Ingrese la edad del Player: ")
                dorsalPlayer = input("Ingrese el numero dorsal del Player: ")
                print(("Seleccione la posicion"))
                for i, pos in enumerate(posiciones):
                    print(f"{i+1}. {pos}")            
                posicionPlayer = posiciones[int(input())-1]

                jugador = [nombrePlayer, edadPlayer, dorsalPlayer, posicionPlayer]
                item[1].append(jugador)
                isAddPlayer = bool(input("Desea agregar otro jugador S(Si) Enter(No)"))

def AddTec(equipos):
    isAddTec = True
    os.system("clear")
    equipo = input("ingrese el nombre del equipo: ").upper()
    for item in equipos:
        if equipo in item:
            while isAddTec:
                os.system("clear")
                cargo = ["Director tecnico", "Asistente Tecnico","Entrenador de arquero","Entrenador"]
                nombreTec = input("Ingrese el nombre del Tecnico: ")
                edadTec = input("Ingrese la edad del Tecnico: ")
                print(("Seleccione el cargo del tecnico"))
                for i, car in enumerate(cargo):
                    print(f"{i+1}. {car}")            
                cargoTec = cargo[int(input())-1]

                tecnico = [nombreTec, edadTec, cargoTec]
                item[2].append(tecnico)
                isAddTec = bool(input("Desea agregar otro Tecnico S(Si) Enter(No)"))
      
def AddMed(equipos):
    isAddMed = True
    os.system("clear")
    equipo = input("ingrese el nombre del equipo: ").upper()
    for item in equipos:
        if equipo in item:
            while isAddMed:
                os.system("clear")
                especialidad = ["Fisioterapeuta", "Camillero","Masajista","Psicologo"]
                nombreMed = input("Ingrese el nombre del Tecnico: ")
                edadMed = input("Ingrese la edad del Tecnico: ")
                print(("Seleccione el cargo del tecnico"))
                for i, car in enumerate(especialidad):
                    print(f"{i+1}. {car}")            
                especMed = especialidad[int(input())-1]

                medico = [nombreMed, edadMed, especMed]
                item[3].append(medico)
                isAddMed = bool(input("Desea agregar otro Medico S(Si) Enter(No)"))

def ShowEnt(equipos):
    os.system("clear")
    print('+','-'*68,'+')
    print("|{:^15}{}{:^20}|".format(' ','LISTADO DE ENTRENADORES POR EQUIPO ',' '))
    print('+','-'*68,'+')
    print("|{:^33} | {:^34}|".format('Nombre Equipo','Nombre del Entrenador'))
    print('+','-'*68,'+')
    for i in equipos:
        for j in i[2]:
            if ("Entrenador" in j):
                print("|{:^33} | {:^34}|".format(i[0],j[0]))
                print('+','-'*68,'+')

partidos = []
def RegistroPartido(equipos):
    cont1 = 1
    cont2 = 1
    selectLocal = []
    selectVisitante = []
    resultado = ""
    os.system("clear")
    print("-------REGISTRO DEL PARTIDO-----")
    print("Ingrese los datos del partido")
    fecha = input("Fecha del juego (dd/mm/aa): ")
    print("Eliga el equipo Local:")
    for i in equipos:
        print(f"{cont1}. {i[0]}")
        cont1 += 1
        selectLocal.append(i)
    local = selectLocal[int(input("Seleccionalo: "))-1]
    print(f"Eliga el equipo visitante del {equipos[equipos.index(local)][1]}:")
    for i in equipos:
        if (local[0] != i[0]):
            print(f"{cont2}. {i[0]}")
            cont2 += 1
            selectVisitante.append(i)
    visitante = selectVisitante[int(input("Seleccionalo: "))-1]
    golLocal = int(input("Goles del equipo local: "))
    golVisitante = int(input("Goles del equipo visitante: "))
    os.system("clear")
    print("-------RESULTADOS-----")
    resultado = 'f"{equipos[local][0]} - {golLocal} - {golVisitante} - {equipos[visitante][0]}"'
    print(f"{equipos[equipos.index(local)][0]} - {golLocal} - {golVisitante} - {equipos[equipos.index(visitante)][0]} \n")
    if (golLocal > golVisitante):
        print(f"Ganador : {equipos[equipos.index(local)][0]}")
        print(f"Perdedor : {equipos[equipos.index(visitante)][0]}")
        equipos[equipos.index(local)][4][1] += 1
        equipos[equipos.index(local)][4][6] += 3

        equipos[equipos.index(visitante)][4][3] += 1
    elif (golLocal < golVisitante):
        print(f"Ganador : {equipos[equipos.index(visitante)][0]}")
        print(f"Perdedor : {equipos[equipos.index(local)][0]}")
        equipos[equipos.index(visitante)][4][1] += 1
        equipos[equipos.index(visitante)][4][6] += 3

        equipos[equipos.index(local)][4][3] += 1
    elif (golLocal == golVisitante):
        print("Empate")            
        equipos[equipos.index(local)][4][2] += 1
        equipos[equipos.index(local)][4][6] += 1
        equipos[equipos.index(visitante)][4][2] += 1
        equipos[equipos.index(visitante)][4][6] += 1

    equipos[equipos.index(local)][4][0] += 1
    equipos[equipos.index(local)][4][4] += golLocal
    equipos[equipos.index(local)][4][5] += golVisitante
    equipos[equipos.index(visitante)][4][0] += 1
    equipos[equipos.index(visitante)][4][4] += golVisitante
    equipos[equipos.index(visitante)][4][5] += golLocal

    save = [fecha, local, visitante, golLocal, golVisitante, resultado]
    print(f"Equipos local: \n {equipos[equipos.index(local)]}")
    print(f"Equipos Visitante: \n {equipos[equipos.index(visitante)]}")
    os.system("sleep 3")

    