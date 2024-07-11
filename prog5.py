import random

def sum_numbers():
    #5.adivinar un numero
    numero_secreto = random.randint(1, 10)
    adivinado = False

    while not adivinado:
        intento = int(input("Adivina el número secreto (entre 1 y 10): "))
        if intento == numero_secreto:
            print("¡Adivinaste! El número secreto es", numero_secreto)
            adivinado = True
        elif intento < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            print("El número secreto es menor. Intenta de nuevo.")
            input("Presiona una tecla para continuar")