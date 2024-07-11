def sum_numbers():
    
    #Calculadoraa de Descuento
    precio_producto = float(input("Ingresa el precio del producto: "))
    porcentaje_descuento = float(input("Ingresa el porcentaje de descuento aplicado: "))
    porcentaje_impuesto = float(input("Ingresa el porcentaje de impuesto sobre las ventas: "))

    precio_descuento = precio_producto - (precio_producto* porcentaje_descuento / 100)

    precio_impuestos = precio_producto + (precio_producto * porcentaje_impuesto / 100)

    print(f"El precio con descuento es: {precio_descuento:.2f} dólares.")
    print(f"El precio final con impuestos incluidos es: {precio_impuestos:.2f} dólares.")
    input(f"preciona una tecla para continua")
