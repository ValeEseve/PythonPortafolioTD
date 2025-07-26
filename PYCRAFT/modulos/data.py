from .colores import RED, YELLOW, GREEN, CYAN, BOLD, RESET

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

# PJS
pjs = [{
    "nombre": f"{CYAN}Ariel, le mague 🧙{RESET}",
    "vida": 100,
    "fuerza": 5,
    "inteligencia": 25,
    "defensa": 5,
    "dado": 8,
    "esta_vivo" : True
},
{
    "nombre": f"{GREEN}Boadicea, la guerrera ⚔️{RESET}",
    "vida": 200,
    "fuerza": 15,
    "inteligencia": 5,
    "defensa": 15,
    "dado": 6,
    "esta_vivo" : True
},
{
    "nombre": f"{YELLOW}Robin, el arquero 🏹{RESET}",
    "vida": 150,
    "fuerza": 15,
    "inteligencia": 15,
    "defensa": 10,
    "dado": 8,
    "esta_vivo" : True
}]

pnj_1 = [
    {"nombre": "Ratón 🐀",
    "vida": 20,
    "fuerza": 5,
    "inteligencia": 1,
    "defensa": 1,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Murciélago 🦇",
    "vida": 20,
    "fuerza": 6,
    "inteligencia": 2,
    "defensa": 1,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Monstruo de baba 😶",
    "vida": 50,
    "fuerza": 6,
    "inteligencia": 1,
    "defensa": 3,
    "dado": 4,
    "esta_vivo" : True},
]

pnj_2 = [
    {"nombre": "Pinganilla 🥷",
    "vida": 50,
    "fuerza": 5,
    "inteligencia": 3,
    "defensa": 3,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Trampero 🥷",
    "vida": 50,
    "fuerza": 6,
    "inteligencia": 4,
    "defensa": 1,
    "dado": 4,
    "esta_vivo" : True},
    {"nombre": "Mago ladrón 🧙‍♂️",
    "vida": 40,
    "fuerza": 6,
    "inteligencia": 7,
    "defensa": 3,
    "dado": 6,
    "esta_vivo" : True},
]

pnj_boss= {
    "nombre": f"{RED}Bug, la Mandamás{RESET} 😠",
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