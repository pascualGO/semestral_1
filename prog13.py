def sum_numbers():
    
    #13. contar vocales en una cadena

    cadena= input("ingresa una cadena de texto:")
    vocales="aeiouaeriou"
    contador = 0

    for caracter in cadena:
        if caracter in vocales:
            contador += 1

    print(f"El número de vocales en la cadena es: {contador}")
    input(f"preciona una tecla para continua")