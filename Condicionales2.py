CatetoA = int(input("Decime el valor de A"))
CatetoB = int(input("Decime el valor de B"))
if CatetoA < 0:
    if CatetoB < 0:
        print("okey")
        Hipotenusa = (CatetoA + CatetoB)**1/2
        print(f"el valor final, con un catetoa de {CatetoA}, Un catetob de {CatetoB} es")
        print(Hipotenusa)
    else:
        print("Error")
