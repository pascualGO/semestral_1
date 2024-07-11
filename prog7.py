def sum_numbers():

    #7. validar entrada

    numero = int(input("Ingrese número positivo: "))

    while numero <= 0:
        print("el numero no es positivo.")
        numero = int(input("Ingrese un número positivo: "))

    print("Número positivo se a ingresado:", numero)

    input(f"preciona una tecla para continua")
            
