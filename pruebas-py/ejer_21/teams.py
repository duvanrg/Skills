equipos = {}
equipo = {
    "Nombre": "Colombia",
    "Jugadores": {
        "1":{
            "Nombre": "James",
            "posicion": "Delantero"
        }
    },
    "Tecnico": [],
    "Medico": [],
    "Datos": {
        "PJ":0,
        "PG":0,
        "PE":0,
        "PP":0,
        "GF":0,
        "GC":0,
        "PUNTOS":0
    }
}

equipo2 = {
    "Nombre": "Colombia",
}

jugadores = {
    "Jugador":{
            "Nombre": "James",
            "posicion": "Delantero"
        }
}

cod = input("Add Code: ")
equipos.update({cod:equipo})
equipos.update({cod:equipo2})
print(equipos)

equipos[cod].update(jugadores)
