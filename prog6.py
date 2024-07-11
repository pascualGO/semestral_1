def sum_numbers():


    #6. Mostrar multiplos de un numero.

    numero = int(input("Ingrese un número entero positivo: "))
    contador = 1

    while contador <= 10:
        print(numero * contador)
        contador += 1
        input(f"preciona una tecla para continua")
