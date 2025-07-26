from modulos.iniciar_juego import setear_pj, mostrar_tutorial
from modulos.combate import comprobar_vida, mostrar_vida, validar_daño, ataque_cuerpo_a_cuerpo, ataque_magico, pj_ataca
from modulos.colores import RED, YELLOW, GREEN, CYAN, BOLD, RESET

# FRASES
pycraft = f"{YELLOW}{BOLD}PYCRAFT{RESET}"
cuerpo_a_cuerpo = f"{GREEN}cuerpo a cuerpo{RESET}"
daño_mágico= f"{CYAN}daño mágico{RESET}"

marco = f"""
{CYAN}╔═══════════════════════════════════════════╗
{CYAN}║       {YELLOW}{BOLD}⚔️  BIENVENID@   A  PYCRAFT ⚔️{RESET}{CYAN}        ║
{CYAN}║                                           ║
{CYAN}║ {GREEN}       Tu aventura comienza aquí...     {CYAN}  ║
{CYAN}╚═══════════════════════════════════════════╝{RESET}
"""

opcion = 0




# Elige un personaje
print(marco)
tutorial= input("¿Deseas leer el tutorial? s/n: ").lower().strip()
if tutorial == "s":
    mostrar_tutorial()

print(f"{"."*15}Ven... avanza hacia la mazmorra{"."*15}\n\n{CYAN}{"*"*60}\n{" "*20}¿Quién eres?\n{"*"*60}\n¿Eres acaso\n{" "*15}1. {pjs[0]["nombre"]}?\nO quizás...\n{" "*15}2. {pjs[1]["nombre"]}?\n¿De verdad eres...\n{" "*15}3. {pjs[2]["nombre"]}?")
opcion_pnj = int(input("Selecciona a tu héroe: "))