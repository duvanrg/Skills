import os
def AddEquipo(equipos):
    os.system("clear")
    teamName = input("Ingrese el nombre del Equipo:").upper()
    myTeam = [teamName,[],[],[],[]]
    equipos.append(myTeam)

def AddPlayer(equipos):
    isAddPlayer = True
    equipo = input("Ingrese el nombre del equipo :").upper()
    for item in equipos:
        if equipo in item:
            while isAddPlayer:
                posiciones = ["Arquero","Defensa","Delantero","Medio Central"]
                nombrePlayer = input("Ingrese el nombre del Player : ")
                edadPlayer =int(input("Ingrese Edad player"))
                dorsalPlayer =int(input("Ingrese el Nro dorsal player"))
                print("Seleccione la posicion del jugador")
                for i,pos in enumerate(posiciones):
                    print(f"{i+1}. {pos}")
                posicionPlayer =posiciones[int(input())-1]
                jugador=[nombrePlayer,edadPlayer,posicionPlayer,dorsalPlayer]
                item[1].append(jugador)
                isAddPlayer = bool(input("Desea agregar otro Jugador S(Si) Enter(No)"))

def AddTenico(equipos):
    isAddTecnico = True
    equipo = input("Ingrese el nombre del equipo :").upper()
    for item in equipos:
        if equipo in item:
            while isAddTecnico:
                cargo = ["Director tecnico","Asistente Tenico","Entrenador De Arquero","Entrenador"]
                nombreTecnico = input("Ingrese el nombre del tecnico : ")
                edadTecnico =int(input("Ingrese Edad tecnico: "))
                print("Seleccione el cargo del director")
                for i,pos in enumerate(cargo):
                    print(f"{i+1}. {pos}")
                cargoTecnico =cargo[int(input())-1]
                tecnico=[nombreTecnico,edadTecnico,cargoTecnico]
                item[2].append(tecnico)
                isAddTecnico = bool(input("Desea agregar otro tecnico S(Si) Enter(No)"))

def AddMedico(equipos):
    isAddMedico = True
    equipo = input("Ingrese el nombre del equipo :").upper()
    for item in equipos:
        if equipo in item:
            while isAddMedico:
                especialidad = ["Fisioterpeuta","Camillero","Masajista","Psicologo"]
                nombreMedico = input("Ingrese el nombre del medico : ")
                edadMedico =int(input("Ingrese Edad medico: "))
                print("Seleccione el cargo del medico")
                for i,pos in enumerate(especialidad):
                    print(f"{i+1}. {pos}")
                cargoMedico =especialidad[int(input())-1]
                medico=[nombreMedico,edadMedico,especialidad]
                item[3].append(medico)
                isAddMedico = bool(input("Desea agregar otro medico S(Si) Enter(No)"))

def mostrarEntrenadores(equipos):
    os.system("clear")
    print('+','-'*68,'+')
    print("|{:^15}{}{:^20}|".format(' ','LISTADO DE ENTRENADORES POR EQUIPO ',' '))
    print('+','-'*68,'+')
    print("|{:^30} | {:^37}|".format('Nombre equipo','Nombre del entrenador '))
    print('+','-'*68,'+')
    for equipo in equipos:
        for tec in equipo[2]:
                if "Director tecnico" in tec:
                    #print(f"{equipo[0]} - {tec[0]}")
                    print("|{:^30} | {:^37}|".format(equipo[0],tec[0]))
                    print('+','-'*68,'+')
    os.system("pause")

