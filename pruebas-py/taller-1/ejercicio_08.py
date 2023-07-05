"""
Crea un programa que pida al usuario ingresar el nombre de un país y luego determine en qué continente se encuentra.Utiliza estructuras condicionales para asociar cada país con su respectivo continente y muestra un mensaje con el
continente correspondiente.
"""
import os

os.system("clear")

africa = ["Argelia", "Angola", "Benín", "Botsuana", "Burkina Faso", "Burundi", "Cabo Verde", "Camerún", "Chad", "Comoras", "Congo", "Costa de Marfil", "Egipto", "Eritrea", "Esuatini", "Etiopía", "Gabón", "Gambia", "Ghana", "Guinea", "Guinea-Bisáu", "Guinea Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar", "Malaui", "Malí", "Marruecos", "Mauricio", "Mauritania", "Mozambique", "Namibia", "Níger", "Nigeria", "República Centroafricana", "República Democrática del Congo", "Ruanda", "Santo Tomé y Príncipe", "Senegal", "Seychelles", "Sierra Leona", "Somalia", "Sudáfrica", "Sudán", "Sudán del Sur", "Tanzania", "Togo", "Túnez", "Uganda", "Yibuti", "Zambia", "Zimbabue"]

america = ["Antigua y Barbuda", "Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Canadá", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Ecuador", "El Salvador", "Estados Unidos", "Granada", "Guatemala", "Guyana", "Haití", "Honduras", "Jamaica", "México", "Nicaragua", "Panamá", "Paraguay", "Perú", "República Dominicana", "San Cristóbal y Nieves", "Santa Lucía", "San Vicente y las Granadinas", "Surinam", "Trinidad y Tobago", "Uruguay", "Venezuela"]

asia = ["Afganistán", "Arabia Saudita", "Armenia", "Azerbaiyán", "Bangladés", "Baréin", "Birmania", "Brunéi", "Bután", "Camboya", "Catar", "China", "Chipre", "Corea del Norte", "Corea del Sur", "Emiratos Árabes Unidos", "Filipinas", "Georgia", "India", "Indonesia", "Irak", "Irán", "Israel", "Japón", "Jordania", "Kazajistán", "Kirguistán", "Kuwait", "Laos", "Líbano", "Malasia", "Maldivas", "Mongolia", "Nepal", "Omán", "Pakistán", "Palestina", "Rusia", "Singapur", "Siria", "Sri Lanka", "Tayikistán", "Tailandia", "Timor Oriental", "Turquía", "Turkmenistán", "Uzbekistán", "Vietnam", "Yemen"]

europa = ["Albania", "Alemania", "Andorra", "Armenia", "Austria", "Azerbaiyán", "Bélgica", "Bielorrusia", "Bosnia y Herzegovina", "Bulgaria", "Chipre", "Ciudad del Vaticano", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia", "España", "Estonia", "Finlandia", "Francia", "Georgia", "Grecia", "Hungría", "Irlanda", "Islandia", "Italia", "Kazajistán", "Letonia", "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia del Norte", "Malta", "Moldavia", "Mónaco", "Montenegro", "Noruega", "Países Bajos", "Polonia", "Portugal", "Reino Unido", "República Checa", "Rumania", "Rusia", "San Marino", "Serbia", "Suecia", "Suiza", "Ucrania"]

oceania = ["Australia", "Fiyi", "Islas Marshall", "Islas Salomón", "Kiribati", "Micronesia", "Nauru", "Nueva Zelanda", "Palaos", "Papúa Nueva Guinea", "Samoa", "Tonga", "Tuvalu", "Vanuatu"]


pais = str(input("Ingrese un pais: "))
if pais in america:
    print(f"el pais {pais} es del continente de America")
elif pais in europa:
    print(f"el pais {pais} es del continente de Europa")
elif pais in asia:
    print(f"el pais {pais} es del continente de Asia")
elif pais in africa:
    print(f"el pais {pais} es del continente de Africa")
elif pais in oceania:
    print(f"el pais {pais} es del continente de Oceania")
else:
    print("el pais que ingreso es incorrecto")






"""


import os

os.system("clear")

selectPais = ""
selectCont = ""
band = 0
cont = [["America",["Colombia","Peru","Brasil","Mexico","Canada","Chile"]],["Europa",["España","Alemania","Francia","Grecia","Italia","Portugal"]],["Asia",["India","China","Corea del Sur","Filipinas","Japón","Rusia"]],["Africa",["Egipto","Marruecos","Somalia","Sudán","Nigeria","Zimbabue"]],["Oceania",["Australia","Islas Salomón","Kiribati","Palaos","Tonga","Nueva Zelanda"]]]

pais = str(input("Ingrese un pais: "))



for i, item in enumerate(cont):
    for j, p in enumerate(item[1]):
        if pais == p:
            selectPais = p
            selectCont = item[0]
            band = 1
            break

if band == 1:
    print(f"el pais {selectPais} es del continente de {selectCont}")

"""
