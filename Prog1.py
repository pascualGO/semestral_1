def sum_numbers():
  #1.Sumar Numeros del 1 al 100

    suma= 0
    contador=1

    while contador <= 100:
        suma += contador
        contador += 1
        
    print(f"la suma de los numeros es: {suma}")

    input(f"preciona una tecla para continua")