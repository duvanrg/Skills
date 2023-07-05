import os

estudiantes = []
isAddStudent = True
opc = 0

while (isAddStudent):
    os.system("clear")
    print("||||||||||||||||||||||||||||||||||||||||||")
    print("||||    SISTEMA REGISTRO DE NOTAS     ||||")
    print("||||||||||||||||||||||||||||||||||||||||||\n")
    print("1.Registrar Alumno","2.Registrar Nota","3.Buscar Alumno","4.Salir", sep="\n")
    opc = int(input("> "))
    if (opc == 1):
        os.system("clear")
        codEst = input("Ingrese el codigo del estudiante: ")
        nombreEst = input("Ingrese el nombre del estudiante: ")
        alumno = [codEst, nombreEst,[],[],[]]
        estudiantes.append(alumno)

    elif (opc == 2):
        opcNotas = "X"
        idx = 0
        os.system("clear")
        search = input("Digite el codigo del alunmo: ")
        for i, item in enumerate(estudiantes):
            if search in item:
                idx = i 
                while (opcNotas.upper() != 'X'):
                    print("|||||||||||||||||||||||||||||||||||||||||||||||||")
                    print("||||    REGISTRO DE NOTAS POR EVALUACION     ||||")
                    print("|||||||||||||||||||||||||||||||||||||||||||||||||\n")

                    print("Q. Registro Quices","T. Registro Talleres","P. Registro Parciales","X. Salir", sep="\n")
                    opcNotas = input("> ")
                    if (opcNotas.upper() == "Q"):
                        estudiantes[idx][3].append(float(input(f"Ingrese el Taller Nro {len(estudiantes[idx][3])+1}")))                        
                    elif (opcNotas.upper() == "T"):
                        estudiantes[idx][4].append(float(input(f"Ingrese el Quiz Nro {len(estudiantes[idx][4])+1}")))
                        os.system("sleep 5")
                    elif (opcNotas.upper() == "P"):
                        estudiantes[idx][2].append(float(input(f"Ingrese el Parcial Nro {len(estudiantes[idx][2])+1}")))
                break
            idx = -1
        if (idx == -1):
            print(f"no se encontro al alumno {search}")     
            os.system("sleep 5")

    elif (opc == 3):
        os.system("clear")
        print("||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||    LISTADOS DE ESTUDIANTES INCRITOS    ||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||\n")
        idx = 0
        search = input("Digite el codigo del alunmo: ")
        for i, item in enumerate(estudiantes):
            if search in item:
                print(estudiantes[i])
                break                
            idx = -1
        if (idx == -1):
            print(f"no se encontro al alumno {search}")      
    elif (opc == 4):
        isAddStudent = False
    else: 
        print("Opcion no valida")
        os.system("sleep 5")



