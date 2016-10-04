def futval():
    print "Aquest programa calcula el valor futur d’una determinada inversio a 10 anys."
    principal = input("Entra la inversio inicial: ")
    apr = input("Entra l’interes anual (exemple:0.5): ")
    anys=input("Entra els anys de la inversió: ")
    for i in range(anys):
        principal = principal * (1 + apr)
    print "La quantitat al cap de",anys,"anys es:", principal
futval()
