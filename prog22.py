def sum_numbers():
    
    # Calcular el salario neto

    salario = float(input("Introduce tu salario bruto: "))

    if salario > 2000:
        salario_neto = salario * 0.8  
        print("Tu salario neto es:", salario_neto)
    else:
        print("Tu salario neto es:", salario)
    input(f"preciona una tecla para continua")
