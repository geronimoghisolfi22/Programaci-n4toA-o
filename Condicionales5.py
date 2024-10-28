Selección = str(input("Bienvenido a Bella Napoli, ¿Qiere una pizza vegetariana? SI/NO"))
if Selección == "SI":
    ingrediente = str(input("Selecciono vegetariano, elija su ingrediente; Tofu o Pimiento"))
    if ingrediente == "Tofu":
        print("Eligio Tofu")
    else:
        print("Eligio Pimiento")
else:
    Ingrediente = str(input("Selecciono no vegetariano, elija su ingrediente; Jamon, peperoni o salmon"))
    if Ingrediente == "Jamon":
        print("Eligio Jamon")
    elif Ingrediente == "Peperoni":
        print("Eligio peperoni")
    else:
        print("Eligio salmon")


