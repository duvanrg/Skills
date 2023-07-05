import os

def AddEquipo(myTeams : dict):
    os.system("cls")
    codTeam = input("Ingrese el Cod del equipo: ").upper()
    teamName = input("Ingrese el nombre del equipo: ").upper()
    #myTeam = [teamName, [], [], [], [0,0,0,0,0,0,0]]
    Equipo = {codTeam:{
        "codTeam": codTeam,
        "Nombre": teamName,
        "Jugadores": {},
        "Tecnico": {},
        "Medico": {},
        "Datos": {
            "PJ":0,
            "PG":0,
            "PE":0,
            "PP":0,
            "GF":0,
            "GC":0,
            "PUNTOS":0
        }
    }
}
    myTeams.update(Equipo)

def ShowEquipos(myTeams: dict):
    os.system("cls")
    print('+','-'*68,'+')
    print("|{:^25}{}{:^26}|".format(' ','LISTADO DE EQUIPOS ',' '))
    print('+','-'*68,'+')
    for cod in myTeams:
        equipo = myTeams.get(cod)
        print("|{:^70}|".format(equipo["Nombre"]))
        print('+','-'*68,'+')
        print("| {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^14} |".format('PJ','PG','PE','PP','GF','GC','PUNTOS'))
        print('+','-'*68,'+')
        print("| {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^14} |".format(equipo["Datos"]["PJ"],equipo["Datos"]["PG"],equipo["Datos"]["PE"],equipo["Datos"]["PP"],equipo["Datos"]["GF"],equipo["Datos"]["GC"],equipo["Datos"]["PUNTOS"]))
        print('+','-'*68,'+')

def AddPlayer(myTeams : dict):
    os.system("cls")
    isAddPlayer = True
    equipo = myTeams.get(input("ingrese el codigo del equipo: ").upper(),-1)
    if (equipo != -1):
        print("El equipo no se encontro")
    else:
        while isAddPlayer:
            os.system("cls")
            posiciones = ["Arquero", "Defensa","Delantero","Medio Central"]
            nombrePlayer = input("Ingrese el nombre del Player: ")
            edadPlayer = int(input("Ingrese la edad del Player: "))
            dorsalPlayer = int(input("Ingrese el numero dorsal del Player: "))
            while (equipo.get("Jugadores",-1) != -1 and equipo["Jugadores"].get(dorsalPlayer, -1)!= -1):
                print("El nro del dorsal ya se encuentra asignado")
                dorsalPlayer = int(input("Ingrese de nuevo el numero dorsal del Player: "))
            print(("Seleccione la posicion"))
            for i, pos in enumerate(posiciones):
                print(f"{i+1}. {pos}")            
            posicionPlayer = posiciones[int(input("> "))-1]

            jugador = {
                "nombrePlayer": nombrePlayer, 
                "edadPlayer": edadPlayer, 
                "dorsalPlayer": dorsalPlayer, 
                "posicionPlayer": posicionPlayer
            }
            
            equipo["Jugadores"].update({dorsalPlayer: jugador})
            
            isAddPlayer = bool(input("Desea agregar otro jugador S(Si) Enter(No)"))

def AddCT(myTeams : dict):
    isAddCT = True
    os.system("cls")
    equipo = myTeams.get(input("ingrese el codigo del equipo: ").upper(),-1)
    print(equipo)
    if (equipo != -1):
        print("El equipo no se encontro")
    else:
        while isAddCT:
            os.system("cls")
            cargo = ["Director tecnico", "Asistente Tecnico","Entrenador de arquero","Entrenador"]
            if (equipo.get("ct",-1) == -1):
                codigo = str(1).zfill(3)
            else:
                codigo = str(len("ct")).zfill(3)
            nombreTec = input("Ingrese el nombre del Tecnico: ")
            edadTec = input("Ingrese la edad del Tecnico: ")
            print(("Seleccione el cargo del tecnico"))
            for i, car in enumerate(cargo):
                print(f"{i+1}. {car}")            
            cargoTec = cargo[int(input("> "))-1]

            cT = {
                "nombreTec": nombreTec, 
                "edadTec": edadTec, 
                "dorsalTec": cargoTec
            }
            
            equipo["Tecnico"].update({codigo: cT})
            
            isAddCT = bool(input("Desea agregar otro Tecnico S(Si) Enter(No)"))

def ShowPlayers(myTeams : dict):
    isAddPlayer = True
    os.system("cls")
    equipo = myTeams.get(input("ingrese el codigo del equipo: ").upper(),-1)
    print(equipo)
    if (equipo != -1):
        print("El equipo no se encontro")
    else:
        if (equipo.get("Jugadores",-1)!= -1):
            pass
        else:
            print(f'no se encontraron jugadores en {equipo["Nombre"]}')

def DeleteTeam(myTeams : dict):
    equipo = myTeams.get(input("Ingrese el codigo del equipo a eliminar: ").upper(), -1)
    if (equipo != -1):
        print(equipo)
        if (bool(input("Desea confirmar la eliminacion Press Enter o n para cancelar: ")) == False):
            delete = myTeams.pop(equipo["codTeam"])
            print(delete)
        else:
            print("El equipo no se elimino")
    else:
        print("El equipo no se encontro")
    os.system("sleep 5")

def EditTeam(myTeams : dict):
    equipo = myTeams.get(input("Ingrese el codigo del equipo a Editar: ").upper(), -1)
    opc = 0
    while (opc != 0):
        print("1. Modificar el Nombre","2. Modificar jugadores","3. Modificar Cuerpo Tecnico","4. Modificar Cuerpo Medico","5. salir", sep=("\n"))
        """print(f'El equipo actual es {equipo["codTeam"]} \n')
        if (bool(input("Presione Enter para modificar el nombre: ")) == False):
            teamname = input("Ingrese el nombre del equipo a Editar: ").upper()
        else:
            teamname = equipo["Nombre"]
        """

        if(opc == 1):
            teamname = input("Ingrese el nombre del equipo a Editar: ").upper()
            equipo = {equipo["codTeam"]:{
                "codTeam": equipo["codTeam"],
                "Nombre": teamname,
                "Jugadores": {},
                "Tecnico": {},
                "Medico": {},
                "Datos": {
                    "PJ":0,
                    "PG":0,
                    "PE":0,
                    "PP":0,
                    "GF":0,
                    "GC":0,
                    "PUNTOS":0
                    }
                }
            }
            print(equipo.keys())