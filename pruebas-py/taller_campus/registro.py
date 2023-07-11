import os
import core
import acudiente as acu

diccPart = {'data':[]}

def LoadDataCliente(args):
    global diccPart
    if (core.CheckData(args)):
        return core.LoadData(args)
    else:
        core.CrearData(args, diccPart)
        return core.LoadData(args)

def MainMenu():
    os.system('clear')
    exit = False
    diccPart = LoadDataCliente("participantes.json")
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('MENU PARTICIPANTES'))
    print ('+','-'*55,'+')
    print("1. Registrar participante","2. Buscar participante","3. Editar participante","4. Eliminar participante","5. Regresar",sep="\n")
    opc = int(input("> "))
    if opc == 1:
        RegistrarParticipante()
    elif opc == 2:
        BuscarParticipante()
    elif opc == 3:
        EditarParticipante()
    elif opc == 4:
        EliminarParticipante()
    elif opc == 5:
        os.system('clear')
        exit = True
    os.system('sleep 3')  

    if (not exit):
        MainMenu()


def RegistrarParticipante():
    os.system('clear')
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('REGISTRO PARTICIPANTES'))
    print ('+','-'*55,'+')
    print('Ingrese los datos del participante')
    data = {
        'NroId': str(input('Id: ')),
        'Nombres': str(input('Nombres: ')),
        'Apellido': str(input('Apellido: ')),
        'Edad': int(input('Edad: ')),
        'Email': str(input('Email: ')),
        'CiudadOri': str(input('Ciudad Origen: ')),
        'Civ': str(input('Estado Civil: ')),
        'Genero': str(input('Genero: ')),
        'Telefono': input('Telefono: ')
    }
    if (data["Edad"]<18):
        print("como el participante es menor de edad debera ingresar los datos del Acudiente"," Esta de acuerdo: ","1. Si","2. No",sep="\n")
        select = int(input("> "))
        if select == 1:
            acudiente = acu.RegistroAcudiente(data['NroId'])
            data.update({'acudiente': acudiente})   
        else:
            print("El participante no se puede registrar sin el acudiente por ser menor de edad")
            os.system("sleep 5")
            return None
    core.CrearData("participantes.json", data)

def BuscarParticipante():
    pass

def EditarParticipante():
    pass

def EliminarParticipante():
    pass





