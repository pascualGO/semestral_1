def sum_numbers():
    
    # Clasificar la categoría de edad

    edad = int(input("Introduce tu edad: "))

    if edad <= 12:
        print("Eres un/a infantil.")
    elif 13 <= edad <= 19:
        print("Eres un/a adolescente.")
    elif 20 <= edad <= 59:
        print("Eres un/a adulto/a.")
    else:
        print("Eres un/a adulto/a mayor.")
    input(f"preciona una tecla para continua")
