from .colores import RED, YELLOW, GREEN, CYAN, BOLD, RESET

# FRASES
pycraft = f"{YELLOW}{BOLD}PYCRAFT{RESET}"
mazmorra =  f"{RED}mazmorra{RESET}"
cuerpo_a_cuerpo = f"{GREEN}cuerpo a cuerpo{RESET}"
daño_mágico= f"{CYAN}daño mágico{RESET}"
marco = f"""
{CYAN}╔═══════════════════════════════════════════╗
{CYAN}║       {YELLOW}{BOLD}⚔️  BIENVENID@   A  PYCRAFT ⚔️{RESET}{CYAN}        ║
{CYAN}║                                           ║
{CYAN}║ {GREEN}       Tu aventura comienza aquí...     {CYAN}  ║
{CYAN}╚═══════════════════════════════════════════╝{RESET}
"""
pj_muerto = f"""
{CYAN}╔═══════════════════════════════════════════╗
{CYAN}║             {YELLOW}{BOLD}💀 HAS MUERTO 💀{RESET}{CYAN}              ║
{CYAN}║                                           ║
{CYAN}║ {GREEN}     Tu aventura llega hasta aquí...    {CYAN}  ║
{CYAN}╚═══════════════════════════════════════════╝{RESET}
"""

# PJS
pjs = [{
    "nombre": f"{CYAN}Ariel, le mague 🧙{RESET}",
    "vida": 100,
    "vida_por_defecto": 100,
    "fuerza": 5,
    "inteligencia": 25,
    "defensa": 5,
    "dado": 6,
    "esta_vivo" : True
},
{
    "nombre": f"{GREEN}Boadicea, la guerrera ⚔️{RESET}",
    "vida": 1,
    "vida_por_defecto": 200,
    "fuerza": 15,
    "inteligencia": 1,
    "defensa": 15,
    "dado": 6,
    "esta_vivo" : True
},
{
    "nombre": f"{YELLOW}Robin, el arquero 🏹{RESET}",
    "vida": 150,
    "vida_por_defecto": 150,
    "fuerza": 15,
    "inteligencia": 10,
    "defensa": 10,
    "dado": 6,
    "esta_vivo" : True
}]

enemigos = [
    [  # Nivel 1
        {"nombre": "Ratón 🐀",
         "vida": 20,
         "fuerza": 5,
         "inteligencia": 1,
         "defensa": 1,
         "dado": 4,
         "esta_vivo": True},
        {"nombre": "Murciélago 🦇",
         "vida": 40,
         "fuerza": 6,
         "inteligencia": 2,
         "defensa": 1,
         "dado": 4,
         "esta_vivo": True},
        {"nombre": "Monstruo de baba 😶",
         "vida": 60,
         "fuerza": 6,
         "inteligencia": 1,
         "defensa": 3,
         "dado": 4,
         "esta_vivo": True}
    ],
    [  # Nivel 2
        {"nombre": "Pinganilla 🥷",
         "vida": 80,
         "fuerza": 5,
         "inteligencia": 3,
         "defensa": 3,
         "dado": 4,
         "esta_vivo": True},
        {"nombre": "Trampero 🥷",
         "vida": 90,
         "fuerza": 6,
         "inteligencia": 4,
         "defensa": 1,
         "dado": 4,
         "esta_vivo": True},
        {"nombre": "Mago ladrón 🧙‍♂️",
         "vida": 80,
         "fuerza": 6,
         "inteligencia": 7,
         "defensa": 3,
         "dado": 6,
         "esta_vivo": True}
    ],
    [  # Boss
        {"nombre": f"{RED}Bug, la Mandamás{RESET} 😠",
         "vida": 100,
         "fuerza": 6,
         "inteligencia": 10,
         "defensa": 3,
         "dado": 8,
         "esta_vivo": True}
    ]
]

pj = {
    "nombre": "",
    "vida": 0,
    "fuerza": 0,
    "inteligencia": 0,
    "defensa": 0,
    "dado": 0,
    "esta_vivo" : True
}