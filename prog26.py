def sum_numbers():
    
    # Comparar dos números

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if num1 > num2:
        print("El primer número es mayor que el segundo.")
    elif num1 < num2:
        print("El segundo número es mayor que el primero.")
    else:
        print("Ambos números son iguales.")
    input(f"preciona una tecla para continua")
