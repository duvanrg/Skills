import os
import core

diccAcudiente = {'data':[]}

def LoadDataAcudiente(args):
    global diccAcudiente
    if (core.CheckData(args)):
        return core.LoadData(args)
    else:
        core.CrearData(args, diccAcudiente)
        return core.LoadData(args)
    
def RegistroAcudiente(idPart):
    os.system('clear')
    diccAcudiente = LoadDataAcudiente("acudiente.json")
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('REGISTRO ACUDIENTES'))
    print ('+','-'*55,'+')
    print('Ingrese los datos del acudiente')
    dataA = {
        'NroId': str(input('Id: ')),
        'Nombres': str(input('Nombres: ')),
        'Parentesco': str(input('Parentesco: ')),
        'participante': idPart
    }
    core.CrearData("acudiente.json", dataA)
    return dataA