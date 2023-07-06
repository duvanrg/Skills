import json
import os

def CrearInfo(args : tuple):
    if(CheckFile(args[0]) == False):
        with open('data/'+args[0], 'w') as write_file:
            json.dump(args[1], write_file, indent = 4)
            write_file.close()
    else:
        if len(args) > 2:
            with open('data/'+args[0], 'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data
                file_data["data"].append(args[2])
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent = 4)
                file.close()

def LoadInfo(fileName):
    if(CheckFile(fileName) == True):
        with open('data/'+fileName, 'r') as read_file:
            dicc = json.load(read_file)
        return dicc

def CheckFile(fileName):
    try:
        with open('data/'+fileName, 'r') as f:
            return True
    except FileNotFoundError as e:
        print("Errr")
        return False
    except IOError as e:
        print(e)
        return False
    