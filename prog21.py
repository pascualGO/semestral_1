def sum_numbers():
    
    # Calcular el precio con descuento

    precio = float(input("Introduce el precio del producto: "))

    if precio > 100:
        precio_descuento = precio * 0.9 
        print("El precio final con descuento es:", precio_descuento)
    else:
        print("El precio final es:", precio)
    input(f"preciona una tecla para continua")
