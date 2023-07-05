"""
en la universidad minuto de dios desean realizar un programa
desean realizar si un estudiante aprobo una determinada 
asignatura, durante el periodo academico los docentes 
pueden realizar quices, talleres y evaluaciones.

cada docente debe realizar minimo 4 quices, 2 talleres y 3 
Evaluaciones por cada estudiante; los quices equivalen al 
35% de la nota final, los talleres equivalen al 15% de la 
nota final. y las evaluaciones equivalen al 50% de la nota 
final

cada docente tiene en su grupo 10 estudiantes matriculados.

el programa debe mostrar al final de la ejecucion el siguiente resumen:

1. total de estudiantes que aprobaron la asignatura
2. total de estudiantes que perdieron la asignatura
3. nombre del estudiante que obtuvo la mayor nota
4. nombre del estudiante que obtuvo la nota mas baja
5. promedio final del grupo
"""



promGrupo = 0
nomMayoNt, nomMenorNt = "", ""
band1, band2 = 0, 0
mayorNt, MenorNt = 0, 0
estApro, estRepro = 0, 0
totalEst = 0
for i in range(1, 11):
    nombre = str(input("ingrese el nombre del estudiante: "))
    qz1  = float(input("ingrese la nota del quiz 1: "))
    qz2  = float(input("ingrese la nota del quiz 2: "))
    qz3  = float(input("ingrese la nota del quiz 3: "))
    qz4  = float(input("ingrese la nota del quiz 4: "))
    tll1 = float(input("ingrese la nota del taller 1: "))
    tll2 = float(input("ingrese la nota del taller 2: "))
    eva1 = float(input("ingrese la nota de la evaluacion 1: "))
    eva2 = float(input("ingrese la nota de la evaluacion 2: "))
    eva3 = float(input("ingrese la nota de la evaluacion 3: "))
    print("#############################################")
    promEst = ((qz1+qz2+qz3+qz4)/4)*0.35+((tll1+tll2)/2)*0.15+((eva1+eva2+eva3)/3)*0.5
    promGrupo += promEst
    if (promEst>mayorNt or band1 == 0):
        nomMayoNt = nombre
        mayorNt = promEst
        band1 = 1
    if (promEst<MenorNt or band2 == 0):
        nomMenorNt = nombre
        MenorNt = promEst
        band2 = 1
    if (promEst >= 3):
        estApro +=1
    else:
        estRepro +=1
    totalEst += 1
print(f"total de estudiantes que aprobaron la asignatura: {estApro}")
print(f"total de estudiantes que reprobaron la asignatura: {estRepro}")
print(f"el estudiante {nomMayoNt} saco la mayor nota con {mayorNt}")
print(f"el estudiante {nomMenorNt} saco la mayor nota con {MenorNt}")
print(f"el promedio del grupo fue {promGrupo/totalEst}")
    

