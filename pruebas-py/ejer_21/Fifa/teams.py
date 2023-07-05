equipos={}
equipo={
    "nombre" : "Colombia",
    "jugadores":{
        "1":{
            "nombre" : "XXXX",
            "posicion":"ffff"
        }
    },

}
equipo2={
    "nombre" : "Argentina",
}
jugador = {
    "jugadores":{
        "1":{
            "nombre" : "XXXX",
            "posicion":"ffff"
        }
    }
}
cod = input("Add code :")
equipos.update({cod:equipo})
equipos.update({cod:equipo2})
equipos["100"].update(jugador)
print(equipos)
