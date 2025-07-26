opcion = 0
mensaje_error= "La opción ingresada no es válida"

print("¡Bienvenid@ al Conversor de Temperatura!")

while True:
    print("Seleccione la opción que corresponda: ")
    try:
        opcion = int(input("""
            1. Convertir Celsius a Fahrenheit.
            2. Convertir Fahrenheit a Celsius.
            3. Salir
            """))
        if opcion <= 0 or opcion > 3:
            print(mensaje_error)
            opcion = 0
    except ValueError:
        print(mensaje_error)
        opcion = 0
    if opcion == 1:
        print()
        try:
            num = int(input("Ingrese la temperatura en °C: "))
            print(f"{num}°C equivalen a {(num * 9/5 + 32):.2f}°F")
        except ValueError:
            print(mensaje_error)
            opcion = 0
    if opcion == 2:
        print()
        try:
            num = int(input("Ingrese la temperatura en °F: "))
            print(f"{num}°F equivalen a {((num - 32) * 5/9):.2f}°C")
        except ValueError:
            print(mensaje_error)
            opcion = 0
    if opcion == 3:
        break

print("¡Gracias por utilizar el Conversor de Temperatura! ¡Hasta pronto!")