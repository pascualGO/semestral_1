def sum_numbers():
        #9. Convertir de decimal a binario

    numero = int(input("Ingrese numero entero: "))

    if numero < 0:
        print("el nuemro no es positivo.")
    else:
        binario = ''
        while numero > 0:
            binario = str(numero % 2) + binario
            numero //= 2

        print(f"El número  binario es: {binario}")
        input(f"preciona una tecla para continua")

