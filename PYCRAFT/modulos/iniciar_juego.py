from .colores import RED, GREEN, CYAN, BOLD, RESET
from .data import pycraft, daño_mágico, cuerpo_a_cuerpo

error = "Opción no válida."
error_opciones= ".. ingrese la opción adecuada, entre 1 y "

def mostrar_tutorial():
    print(f"{CYAN}{"*"*60}\n")
    print(f"En {pycraft} tu objetivo es avanzar a través de una mazmorra repleta de enemigos sedientos de sangre. \n{BOLD}¿Lograrás derrotar a {RED}'Bug, la Mandamás 😠'?{RESET} \nLos personajes (tanto el tuyo como los enemigos) pueden atacar {cuerpo_a_cuerpo} o con {daño_mágico}.\nLos ataques {cuerpo_a_cuerpo} se calculan lanzando un dado y multiplicando su resultado con la {GREEN}fuerza{RESET} del personaje. \nCon el {daño_mágico}, se utiliza {CYAN}inteligencia{RESET}.\nCada personaje al recibir daño {cuerpo_a_cuerpo} utilizará su {GREEN}defensa{RESET} para mitigar el daño. \nEn el caso del {daño_mágico}, el personaje utilizará su {CYAN}inteligencia{RESET}.")
    print(f"\n{CYAN}{"*"*60}\n")
    input()


def validar_opcion(opciones):
    while True:
        try:
            opcion = int(input())
            if 1 <= opcion <= opciones:
                return opcion
            else:
                print(f"{error}{error_opciones}{opciones}")
        except ValueError:
            print(error)
