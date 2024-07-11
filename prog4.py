def sum_numbers():
    
        #4.Sumar digitos de un numero

    numero = int(input("ingrese numero entero: "))
    sd= 0

    while numero > 0:
        sd += numero % 10
        numero //=10
        
    print(f"la suma de los digitos son {sd}")
    input(f"preciona una tecla para continua")
    

    
