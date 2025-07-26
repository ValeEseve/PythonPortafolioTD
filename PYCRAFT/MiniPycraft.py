from modulos.iniciar_juego import setear_pj, mostrar_tutorial, validar_opcion
from modulos.combate import comprobar_vida, pj_ataca
from modulos.colores import RED, YELLOW, GREEN, CYAN, BOLD, RESET
from modulos.data import pj, pjs, pnj_1, pnj_2, pnj_boss, marco, pycraft, cuerpo_a_cuerpo, daño_mágico

opcion = 0

# print(marco)
# tutorial= input("¿Deseas leer el tutorial? s/n: ").lower().strip()
# if tutorial == "s":
#     mostrar_tutorial()

# print(f"{"."*15}{RED}Ven... avanza hacia la mazmorra{RESET}{"."*15}\n\n{"*"*60}\n{" "*20}¿Quién eres?\n{"*"*60}\n¿Eres acaso\n{" "*15}1. {pjs[0]["nombre"]}?\nO quizás...\n{" "*15}2. {pjs[1]["nombre"]}?\n¿De verdad eres...\n{" "*15}3. {pjs[2]["nombre"]}?")
# print("Selecciona a tu héroe: ")
# opcion_pnj = validar_opcion(3)
# pj = pjs[opcion_pnj]
# print(f"{"."*15}\n\n¿Así que eres {pj["nombre"]}? Que bueno que estés aquí.\n{pnj_boss["nombre"]} está amenazando el pueblo con constantes robos.\nSabemos dónde se esconde... ¿podrías ir a buscarle y enseñarle que no debe meterse con nosotros?\nBueno... no es como que tengas una alternativa...\nAl fin y al cabo, eres {pj["nombre"]}, muy valiente y capaz, y de eso se trata este juego ¿cierto?\n¿Es esta o no la realidad? Quién sabe...")
# input(f"{RED}Entrar a la mazmorra...{RESET}")

pj = pjs[0]

for enemigo in pnj_1:
    print(f"Te adentras en la {RED}mazmorra{RESET} y ¡¡se abalanza contra ti un gran y horrible {enemigo["nombre"]}!!")
    while True:
        if enemigo["vida"] > 0:
            pj_ataca(pj, enemigo)
            if pj["vida"] > 0 and enemigo["vida"] > 0:
                pj_ataca(enemigo, pj)
            else:
                break
        else:
            break
