def sum_numbers():
    
    # Verificar si un nombre es corto, mediano o largo

    nombre = input("Introduce un nombre: ")

    longitud = len(nombre)

    if longitud < 5:
        print("El nombre es corto.")
    elif 5 <= longitud <= 8:
        print("El nombre es mediano.")
    else:
        print("El nombre es largo.")
    input(f"preciona una tecla para continua")
