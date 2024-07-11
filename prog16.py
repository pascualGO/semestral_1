def sum_numbers():
    
    #16. sumar los primeros N numeros naturales

    N = int(input("Ingrese número entero: "))
    suma = 0


    for i in range ( 1 , N + 1 ):
        suma += i

    print(f" la suma de los primeros {N} numeros naturales son:{suma}")
    input(f"preciona una tecla para continua")
