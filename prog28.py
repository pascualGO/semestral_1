def sum_numbers():
    
    # Determinar la categoría de un trabajador

    experiencia = float(input("Introduce los años de experiencia: "))

    if experiencia < 2:
        print("Categoría: Junior")
    elif 2 <= experiencia <= 5:
        print("Categoría: Semi-Senior")
    else:
        print("Categoría: Senior")
    input(f"preciona una tecla para continua")
