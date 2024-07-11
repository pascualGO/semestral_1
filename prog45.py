def sum_numbers():
    
    #Calculadoraa de Salario
    horas_trabajadas = float(input("Ingresa las horas trabajadas en el mes: "))
    salario_por_hora = float(input("Ingresa el salario por hora: "))
    horas_extra = float(input("Ingresa el número de horas extra trabajadas (si las hay): "))

    salario_total = horas_trabajadas * salario_por_hora
    salario_extra = horas_extra * (salario_por_hora * 2)
    salario_total += salario_extra

    print(f"El salario mensual total es: {salario_total:.2f} dólares.")
    print(f"El monto adicional por horas extra es: {salario_extra:.2f} dólares.")
    input(f"preciona una tecla para continua")
