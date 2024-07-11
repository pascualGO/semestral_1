def sum_numbers():
    
    # Determinar si un año es un siglo

    anio = int(input("Introduce un año: "))

    if anio % 100 == 0:
        print("El año", anio, "es el primer año de un siglo.")
    else:
        print("El año", anio, "no es el primer año de un siglo.")
    input(f"preciona una tecla para continua")
