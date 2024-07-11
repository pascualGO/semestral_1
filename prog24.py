def sum_numbers():
    
    # Clasificar el IMC

    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print("Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Normal")
    elif 25 <= imc < 29.9:
        print("Sobrepeso")
    else:
        print("Obesidad")
    input(f"preciona una tecla para continua")
