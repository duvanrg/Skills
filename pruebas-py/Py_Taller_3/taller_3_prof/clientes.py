import core 
import os

def CreateData(*args):
    core.CrearInfo(args)

def LoadData(*args):
    return core.LoadInfo("clientes.json")