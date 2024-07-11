def sum_numbers():
    
    # Calcular la tarifa de un taxi

    distancia = float(input("Introduce la distancia recorrida en kilómetros: "))

    if distancia <= 10:
        tarifa = 2.50 * distancia
    else:
        tarifa = 2.50 * 10 + 2.00 * (distancia - 10)

    print("La tarifa del taxi es: $", tarifa)
    input(f"preciona una tecla para continua")
