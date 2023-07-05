"""

artm = []
group = input("ingrese el nombre para el grupo artemis \ndebe tener una letra mayuscula y un digito: ")

artm.append(group)
artm.append([])

print(artm)

nombre = str(input("Nombre: "))
apellidos = str(input("Apellidos: "))
doc = int(input("Documento: "))
tipoDoc = str(input("Tipo Documento (CC/TI/DNI/CI): "))
calificaciones = []
camper = [nombre, apellidos, doc, tipoDoc, calificaciones]
artm[1].append(camper)


print(artm.index("J2")+1)


os.system("cls")
j = ["estados unidos","Grupo A",7,5,1,2,20,5,16]
print('+', '-'*66, '+') 
print("|{:^30}{}{:^31}|".format(' ','Grupo A',' '))
print('+', '-' *66, '+')

print(f'''| {j[0]:^18}|{j[2]:^6}|{j[3]:^6}|{j[4]:^6}|{j[5]:^6}|{j[6]:^6}|{j[7]:^6}|{j[8]:^6}|''')
print('+', '-' *66, '+')

"""
import os

grupos = [[["Grupo A", "Cali",[10]],["Grupo B", "Medellin", [8]]],[["Grupo C","Bucaramanga", [10]],["Grupo D", "Bogota", [12]]]]
grupo = ""
y = True

print(grupos[1][1][2])

