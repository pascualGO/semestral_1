def sum_numbers():
    
    # Verificar si un número es positivo, negativo o cero
    numero = float(input("Introduce un número: "))

    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
    input(f"preciona una tecla para continua")
