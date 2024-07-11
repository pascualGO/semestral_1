def sum_numbers():
    
    # Verificar si un triángulo es válido

    lado1 = float(input("Introduce la longitud del primer lado del triángulo: "))
    lado2 = float(input("Introduce la longitud del segundo lado del triángulo: "))
    lado3 = float(input("Introduce la longitud del tercer lado del triángulo: "))

    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("El triángulo es válido.")
    else:
        print("El triángulo no es válido.")
    input(f"preciona una tecla para continua")
