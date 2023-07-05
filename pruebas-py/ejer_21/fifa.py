import torneoFifa as equipos
import os

if __name__ == "__main__":
    teams = {}
    isAddTeam = True
    opcion = 0
    while isAddTeam:
        os.system("cls")
        print("1. Registrar equipo","2. Mostrar equipos","3. Registro de jugadores","4. Registro cuerpo Tecnico","5. Registro Cuerpo Medico","6. Mostrar jugadores por equipos","7. Registro partidos", sep="\n")
        try:
            opcion = int(input("> "))
            if(opcion == 1):
                equipos.AddEquipo(teams)
            elif(opcion == 2):
                print(teams)
            elif(opcion == 3):
                equipos.AddPlayer(teams)
            elif(opcion == 4):
                equipos.AddTec(teams)
            elif(opcion == 5):
                equipos.AddMed(teams)
            elif(opcion == 6):
                equipos.ShowPlayers(teams)
            elif(opcion == 7):
                equipos.RegistroPartido(teams)
        except Exception:
            print("No se reconoce el tipo de dato del valor ingresado")
            os.system("PAUSE")
        else:
            isAddTeam = bool(input("Desea continuar en el programa S(Si) o Enter(No) "))