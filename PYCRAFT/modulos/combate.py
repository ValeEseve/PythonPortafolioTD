from .colores import RED, RESET
from .iniciar_juego import validar_opcion
from .data import pj, pjs, cuerpo_a_cuerpo, daño_mágico, pj_muerto
import random

def comprobar_vida(pj):
    if pj["vida"] > 0:
        return True
    print(f"{RED}{pj["nombre"]} ha muerto.{RESET}")
    if pj in pjs:
        print(pj_muerto)
    return False

def mostrar_vida(pj):
    print(f"{pj["nombre"]} tiene {pj["vida"]} puntos de vida")

def validar_daño(daño):
    if daño < 0:
        return 0
    return daño

def ataque_cuerpo_a_cuerpo(pj1, pj2):
    daño = pj1["fuerza"] * random.randint(1, pj1["dado"] + 1)
    daño = validar_daño(daño)
    pj2["vida"] -= daño - pj2["defensa"]
    print(f"{pj1["nombre"]} le inflinge {daño} puntos de daño {cuerpo_a_cuerpo} a {pj2["nombre"]}")

def ataque_magico(pj1, pj2):
    daño = pj1["inteligencia"] * random.randint(1, pj1["dado"] + 1)
    daño = validar_daño(daño)
    pj2["vida"] -= daño - pj2["inteligencia"]
    print(f"{pj1["nombre"]} le inflinge {daño} puntos de {daño_mágico} a {pj2["nombre"]}")

def pj_ataca(pj1, pj2):
    print(f"{pj1["nombre"]} se prepara para atacar a {pj2["nombre"]}.")
    if pj1 in pjs:
        print("""
        1. Atacar cuerpo a cuerpo (usar fuerza).
        2. Atacar con un hechizo (usar inteligencia).
        """)
        opcion_ataque = validar_opcion(2)
    else:
        opcion_ataque= random.randint(1, 2)
    if opcion_ataque == 1:
        ataque_cuerpo_a_cuerpo(pj1, pj2)
        pj2["esta_vivo"] = comprobar_vida(pj2)
    if opcion_ataque == 2:
        ataque_magico(pj1, pj2)
        pj2["esta_vivo"] = comprobar_vida(pj2)
    mostrar_vida(pj2)