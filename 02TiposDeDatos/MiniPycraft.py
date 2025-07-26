import random

opcion = 0
pjs = [{
    "nombre": "Ariel, le mague",
    "vida": 100,
    "fuerza": 5,
    "inteligencia": 25,
    "defensa": 5,
    "dado": 8,
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
    "inteligencia": 3,
    "defensa": 3,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Trampero",
    "vida": 50,
    "fuerza": 6,
    "inteligencia": 4,
    "defensa": 1,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Mago ladrón",
    "vida": 40,
    "fuerza": 6,
    "inteligencia": 7,
    "defensa": 3,
    "dado": 6,
    "esta_vivo" : True},
]

pnj_boss= {
    "nombre": "Bug, la Mandamás",
    "vida": 100,
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

def comprobar_vida(pj):
    if pj["vida"] > 0:
        return True
    print(f"{pj["vida"]} ha muerto.")
    return False

def validar_daño(daño):
    if daño < 0:
        return 0
    return daño

def ataque_cuerpo_a_cuerpo(pj1, pj2):
    daño = pj1["fuerza"] * random.randint(0, pj1["dado"] + 1)
    daño = validar_daño(daño)
    pj2["vida"] -= daño - pj2["defensa"]
    print(f"{pj1["nombre"]} le inflinge {daño} puntos de daño cuerpo a cuerpo a {pj2["nombre"]}")

def ataque_magico(pj1, pj2):
    daño = pj1["inteligencia"] * random.randint(0, pj1["dado"] + 1)
    daño = validar_daño(daño)
    pj2["vida"] -= daño - pj2["inteligencia"]
    print(f"{pj1["nombre"]} le inflinge {daño} puntos de daño mágico a {pj2["nombre"]}")

def pj_ataca(pj1, pj2):
    print(f"{pj1["nombre"]} se prepara para atacar a {pj2["nombre"]}.")
    opcion_ataque = int(input("""
    1. Atacar cuerpo a cuerpo (usar fuerza).
    2. Atacar con un hechizo (usar inteligencia).
    """))
    if opcion_ataque == 1:
        ataque_cuerpo_a_cuerpo(pj1, pj2)
        comprobar_vida(pj2)
    if opcion_ataque == 2:
        ataque_magico(pj1, pj2)
        comprobar_vida(pj2)


