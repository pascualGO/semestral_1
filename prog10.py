def sum_numbers():
    
    #10. simular un cajero automatico

    pin_correcto = "2605"
    intentos = 3
    bloqueado = False

    while intentos > 0:
        pin = input("Ingrese su PIN: ")
        if pin == pin_correcto:
            print("PIN correcto")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"PIN incorrecto tiene {intentos} intentos.")
            else:
                bloqueado = True

    if bloqueado:
        print("Tres intentos fallidos Su tarjeta ha sido bloqueada.")
        input(f"preciona una tecla para continua")
