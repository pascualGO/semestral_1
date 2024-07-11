def sum_numbers():
    
    # Determinar si un número es divisible por 3 y 5

    numero = int(input("Introduce un número: "))

    if numero % 3 == 0 and numero % 5 == 0:
        print("El número es divisible por 3 y 5.")
    elif numero % 3 == 0:
        print("El número es divisible por 3 pero no por 5.")
    elif numero % 5 == 0:
        print("El número es divisible por 5 pero no por 3.")
    else:
        print("El número no es divisible por 3 ni por 5.")
    input(f"preciona una tecla para continua")
