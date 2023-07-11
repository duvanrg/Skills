"""
el centro de entrenamiento de campus desea realizar un programa que le permita llevar el control de los candidatos a participar en su programa de entrenamiento, campus desea realizar un registro previo de los participantes; la informacion que se comtempla por cada participante es la siguiente: nro de ID, nombres, apellidos, edad, Email, ciudad de origen, estado civil, genero, telefono.

los campers que son menores de edad deben registrar informacion de acudientes con la siguiente informacion: id acudiente, nombre acudiente, parentesco acudiente. 

la informacion ingresada debe ser almacenada de forma local
"""
import os
import registro as reg

if __name__ == '__main__':
    opc = 0
    run = True
    while run:
        os.system('clear') 
        print ('+','-'*55,'+')
        print ('|{:^57}|'.format('BIENVENIDO A CAMPUS'))
        print ('+','-'*55,'+')
        print ("1. Registrar participante","2. Listar participantes","3. Salir",sep="\n")
        opc = int(input("> "))
        if opc == 1:
            reg.MainMenu()
        elif opc == 2:
            pass
        elif opc == 3:
            run = False
