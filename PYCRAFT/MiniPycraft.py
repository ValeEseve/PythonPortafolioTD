from modulos.iniciar_juego import setear_pj, mostrar_tutorial, validar_opcion
from modulos.combate import comprobar_vida, pj_ataca
from modulos.colores import RED, YELLOW, GREEN, CYAN, BOLD, RESET
from modulos.data import pj, pjs, enemigos, mazmorra, marco

opcion = 0

print(marco)
tutorial= input("¿Deseas leer el tutorial? s/n: ").lower().strip()
if tutorial == "s":
    mostrar_tutorial()

print(f"{"."*15}{RED}Ven... avanza hacia la mazmorra{RESET}{"."*15}\n\n{"*"*60}\n{" "*20}¿Quién eres?\n{"*"*60}\n¿Eres acaso\n{" "*15}1. {pjs[0]["nombre"]}?\nO quizás...\n{" "*15}2. {pjs[1]["nombre"]}?\n¿De verdad eres...\n{" "*15}3. {pjs[2]["nombre"]}?")
print("Selecciona a tu héroe: ")
opcion_pnj = validar_opcion(3)
pj = pjs[opcion_pnj - 1]
print(f"{"."*15}\n\n¿Así que eres {pj["nombre"]}? Que bueno que estés aquí.\n{enemigos[2][0]["nombre"]} está amenazando el pueblo con constantes robos.\nSabemos dónde se esconde... ¿podrías ir a buscarle y enseñarle que no debe meterse con nosotros?\nBueno... no es como que tengas una alternativa...\nAl fin y al cabo, eres {pj["nombre"]}, muy valiente y capaz, y de eso se trata este juego ¿cierto?\n¿Es esta o no la realidad? Quién sabe...")
input(f"{RED}Entrar a la mazmorra...{RESET}\n\n")

pj = pjs[1]
nivel_mazmorra = 1

for i, nivel in enumerate(enemigos):
    print(f"{"*"*10}{BOLD}Te encuentras en el nivel {nivel_mazmorra} de la {mazmorra}{"*"*10}{RESET}\n\n")
    for enemigo in nivel:
        print(f"{"*"*5}Te adentras en la {mazmorra} y ¡¡se abalanza {enemigo["nombre"]} contra ti!!\n")
        while enemigo["esta_vivo"]:
            if enemigo["esta_vivo"]:
                pj_ataca(pj, enemigo)
            else:
                print("pj_muerto")
                break
            if pj["esta_vivo"] and enemigo["esta_vivo"]:
                pj_ataca(enemigo, pj)
                if pj["esta_vivo"] == False:
                    break
        if pj["esta_vivo"] == False:
            break
    if pj["esta_vivo"] == False:
            break
    elif nivel_mazmorra < 3:
        print("Avanzas al siguiente nivel...\n")
    nivel_mazmorra += 1
print()