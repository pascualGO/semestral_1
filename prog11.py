def sum_numbers():
    
        #12. sumar numeros pares del 1 al 100

    suma_pares = 0

    for i in range (2, 101 , 2):
        suma_pares += i

    print(f"la suma de los numeros del 1 al 100 es:{suma_pares}")
    input(f"preciona una tecla para continua")
