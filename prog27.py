def sum_numbers():
    
    # Determinar el tipo de licencia de conducir

    edad = int(input("Introduce tu edad: "))

    if 16 <= edad <= 17:
        print("Licencia de menor")
    elif 18 <= edad <= 65:
        print("Licencia de adulto")
    else:
        print("Licencia de adulto mayor")
    input(f"preciona una tecla para continua")
