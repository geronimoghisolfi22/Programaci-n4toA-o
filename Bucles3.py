PIN_SECRETO = 3215
i = 3
while i > 0:
    str(input("Ingrese la contraseña"))
    if PIN_SECRETO == PIN_SECRETO:
        print("Longin Correcto")
    elif i < 0:
        print("Llamando a la policia")
        break
    else:
        i -= 1
        print(f"Error, intente de vuelta, restan {i} intentos")