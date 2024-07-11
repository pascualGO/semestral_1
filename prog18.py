def sum_numbers():
    
    #18. convertir grados Celsius a Fahrenheit

    inicio = int(input("La temperatura inicial grados Celsius: "))
    fin = int(input("La temperatura final grados Celsius: "))

    print("Conversión:")
    for C in range(inicio, fin + 1):
        F = (C * 9/5) + 32
        print(f"{C}C = {F}F")
    input(f"preciona una tecla para continua")
