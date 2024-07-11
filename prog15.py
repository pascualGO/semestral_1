def sum_numbers():
    
    #15. imprimir numeros impares hasta el numero dado

    numero=int(input("ingrese un numero entero: "))

    print(f"numeros impares del 1 al {numero}:")

    for i in range (1 , numero + 1 , 2 ):
        print(i)
    input(f"preciona una tecla para continua")
