
import os
totalAprobados=0
totalReprobados=0
notaFinalMax=0.0
notaFinalMin=5.3
estudianteNotaMayor = 0
estudianteNotaMenor = 0
tQuices=4
totalParciales = 3
totalTalleres =2
promedioGeneral = 0
totalEstudiantes = 2

for i in range(0,totalEstudiantes):
    acumuladorQuiz=0
    acumuladorTaller=0
    acumuladorParcial=0
    nombre = input("Ingrese el nombre del estudiante: ")
    for j in range(0,4):
        if (j<=3):
            acumuladorQuiz += float(input(f'Ingrese la nota del Quiz Nro:{j+1}: '))
        if (j <=2):
            acumuladorParcial += float(input(f'Ingrese la nota del Parcial Nro:{j+1}: '))
        if (j<=1):
            acumuladorTaller += float(input(f'Ingrese la nota del Talle Nro: {j+1}: '))
    promedio = ((acumuladorQuiz/4)*0.35) + ((acumuladorParcial/3))*0.5 + ((acumuladorTaller/3)*0.15)
    if (promedio<3.0): 
        totalReprobados +=1
    else:
        totalAprobados +=1
    promedioGeneral +=promedio 
    if (promedio < notaFinalMin): 
        estudianteNotaMenor = nombre 
        notaFinalMin = promedio 
        notaMenor=promedio
    elif (promedio > notaFinalMax): 
        estudianteNotaMayor = nombre
        notaFinalMax = promedio 
        notaMayor = promedio

print(f'El total de estudiantes aprobados: {totalAprobados}')
print(f'El total de estudiantes reprobados: {totalReprobados}')
print(f'El estudiante con mayor nota es: {estudianteNotaMayor}')
print(f'El estudiante con menor nota es : {estudianteNotaMenor}')
print(f'El promedio general del grupo es: {promedioGeneral/totalEstudiantes}')
print(f'La nota mas alta es : {notaMayor} y la mas baja es : {notaMenor}')
    