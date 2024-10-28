edad = int(input("Decime tu edad y te digo si podes pasar!"))
acompañado = str(input("Indica si esta acompañado con si o no: "))
if edad>= 18:
    if acompañado =="Si":
        print("Podes pasar")
    else:
        print("No podes pasar")
else:
    print("No podes pasar")