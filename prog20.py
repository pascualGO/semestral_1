def sum_numbers():
    
    #20.repetir una cadena

    cadena = input("cadena de texto: ")
    N = int(input("Ingrese número entero: "))

    print(f" La cadena '{cadena}' se repetira {N} veces:")
    for i in range(N):
        print(cadena)
    input(f"preciona una tecla para continua")
