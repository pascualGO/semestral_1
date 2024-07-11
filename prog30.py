def sum_numbers():
    
    # Determinar si un carácter es una letra o un dígito

    caracter = input("Introduce un carácter: ")

    if caracter.isalpha():
        print("El carácter ingresado es una letra.")
    elif caracter.isdigit():
        print("El carácter ingresado es un dígito.")
    else:
        print("El carácter ingresado no es ni una letra ni un dígito.")
    input(f"preciona una tecla para continua")
