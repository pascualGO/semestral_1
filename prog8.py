def sum_numbers():
    
    #8. Contador de digitos

    numero = int(input("Ingrese numero entero: "))
    contador_digitos = 0

    while numero != 0:
        numero //= 10
        contador_digitos += 1

    print("El número tiene", contador_digitos, "dígitos.")
    input(f"preciona una tecla para continua")
