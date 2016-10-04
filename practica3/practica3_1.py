def mentre():
    n = input("Diga'm un nombre natural: ")
    m = 1
    m2 = 1
    contador = 0
    contador2 = 0 
    contador3 = 0
    
    while m <= n:
        contador+=m
        m+=1
    print "La suma dels termes fins a aquest nombre es:",contador

    while m2 <= n:
        contador2+=m2
        m2+=2
    print "La suma dels termes imparells fins a aquest nombre es:",contador2
    print " "

    x = input("Digui'm els nombres seguits per un intro que vol sumar i si has acabat, posa 999: ")
    while x != 999:
        contador3+=x
        x = input("Digui'm els nombres seguits per un intro que vol sumar i si has acabat, posa 999: ")
    print "La seva suma és:",contador3
mentre()
