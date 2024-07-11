def sum_numbers():
    
    #17. determinar si un numero es primo

    numero = int(input("Ingrese número entero: "))
    es_primo = True


    if numero > 1:
        
        for  i  in  range ( 2, int(numero**0.5)+ 1):
            if numero % i == 0:
                es_primo = False
                break

    else:
        es_primo = False

    if es_primo:
        print(f"{numero} es número primo.")
    else:
        print(f"{numero} no es número primo.")
    input(f"preciona una tecla para continua")
