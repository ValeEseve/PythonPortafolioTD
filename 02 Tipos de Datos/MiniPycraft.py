import random

opcion = 0
pjs = [{
    "nombre": "Ariel, le mague",
    "vida": 100,
    "fuerza": 10,
    "inteligencia": 25,
    "defensa": 5,
    "dado": 10,
    "esta_vivo" : True
},
{
    "nombre": "Boadicea, la guerrera",
    "vida": 200,
    "fuerza": 15,
    "inteligencia": 5,
    "defensa": 15,
    "dado": 6,
    "esta_vivo" : True
},
{
    "nombre": "Robin, el arquero",
    "vida": 150,
    "fuerza": 15,
    "inteligencia": 15,
    "defensa": 10,
    "dado": 8,
    "esta_vivo" : True
}]

pnj_1 = [
    {"nombre": "Rata",
    "vida": 20,
    "fuerza": 5,
    "inteligencia": 1,
    "defensa": 1,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Murciélago",
    "vida": 20,
    "fuerza": 6,
    "inteligencia": 2,
    "defensa": 1,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Baba con conciencia",
    "vida": 50,
    "fuerza": 6,
    "inteligencia": 1,
    "defensa": 3,
    "dado": 4,
    "esta_vivo" : True},
]

pnj_2 = [
    {"nombre": "Pinganilla",
    "vida": 50,
    "fuerza": 5,
    "inteligencia": 7,
    "defensa": 3,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Trampero",
    "vida": 50,
    "fuerza": 6,
    "inteligencia": 5,
    "defensa": 1,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Mago ladrón",
    "vida": 40,
    "fuerza": 6,
    "inteligencia": 10,
    "defensa": 3,
    "dado": 6,
    "esta_vivo" : True},
]

pnj_boss= {
    "nombre": "Bug, la Mandamás",
    "vida": 150,
    "fuerza": 6,
    "inteligencia": 10,
    "defensa": 3,
    "dado": 8,
    "esta_vivo" : True
}

pj = {
    "nombre": "",
    "vida": 0,
    "fuerza": 0,
    "inteligencia": 0,
    "defensa": 0,
    "dado": 0,
    "esta_vivo" : True
}

def pj_atacar(enemigo):
    print(f"{pj["nombre"]} ataca a {enemigo["nombre"]}.")