def inversio():
    inversio = input("Digues la inversio amb la qual es vol treballar: ")
    inversio2 = 2*inversio
    interes = input("Digues el interes (exemple: 0.12) : ")
    anys = 0
    while inversio < inversio2:
        inversio = inversio * (1+interes)
        anys+=1
    print "La seva inversio es duplicará en:",anys,"anys"
inversio()
