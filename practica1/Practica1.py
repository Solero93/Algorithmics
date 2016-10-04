# ALGORÍSMICA: Pràctica 1
# Escrit per:  

import math
import cmath

# Programa per calcular l'interés simple d'una inversió
def futval():
    print "PROGRAMA A"
    print "Aquest programa calcula el valor futur de una determinada inversio a 10 anys."
    principal = input("Entra la inversio inicial: ")
    apr = input("Entra interes anual (exemple:0.05) : ")
    anys=input("Entra els anys de la inversio: ")
    for i in range(anys):
        principal=principal*(1+apr)
    print "La quantitat al cap de",anys,"anys es:", principal
    print " "

# Programa que representa la taula de 0°C-100°C de 10 en 10 i el seu equivalent en graus Fahrenheit
def convert():
    print "PROGRAMA B"
    print "Taula de Conversio de Celsius a Fahrenheit de 1-10"
    for x in range(0,101,10):
        celsius=x
        fahrenheit=9.0/5.0*celsius+32
        print repr(celsius),"C ", repr(fahrenheit),"F "
    print " "

# Programa que representa una sèrie d'operacions amb els seus resultats corresponents   
def exp():
    print "PROGRAMA C"
    print "Resultats de una serie de operacions"
    print "4.0 / 10.0 + 3.5 * 2 =",4.0/10.0+3.5*2
    print "10%4 + 6/2 =",10%4+6/2
    print "abs(4-20/3) ** 3 =",abs(4-20.0/3)**3.0
    print "sqrt(4.5-5.0) + 7*3 =",cmath.sqrt(4.5j-5.0j)+7*3
    print "3 * 10 /3 + 10%3 =",3*10/3+10%3
    print "3L ** 3 =",long(long(3L)**3)
    print " "
    
# Programa per calcular el pendent de la recta que defineixen dos punts dins d'un mateix pla
def punts():
    print "PROGRAMA D"
    print "Calcul del pendent de la recta que defineixen dos punts qualsevols del mateix pla"
    a,b=input ("Posa'm les coordenades del primer punt separades per una coma: ")
    c,d=input ("Posa'm les coordenades del segon punt separades per una coma: ")
    if c==a:
        print "El seu pendent tendeix a l'infinit, ja que estan alineats verticalment"
    else:
        pendent=((float(d-b))/(float(c-a)))
        print "El pendent de la recta que defineixen es de: ",pendent," unitats"
    print " "
    
# Programa per calcular la distancia euclideana entre dos punts qualsevols del mateix pla
def euclid():
    print "PROGRAMA E"
    print "Calcul de la distancia euclideana entre dos punts qualsevols del mateix pla"
    a,b=input ("Posa'm les coordenades del primer punt separades per una coma: ") 
    c,d=input ("Posa'm les coordenades del segon punt separades per una coma: ")
    dist=math.sqrt(((c-a)**2)+((d-b)**2))
    print "La distancia entre aquests punts es de: ",dist," unitats"
    print " "

# Programa per calcular el nombre enter de la distancia euclideana entre dos punts qualsevols del mateix pla
def euclid2():
    print "PROGRAMA F"
    print "Calcul del nombre enter de la distancia euclideana entre dos punts qualsevols del mateix pla"
    a,b=input ("Posa'm les coordenades del primer punt separades per una coma: ") 
    c,d=input ("Posa'm les coordenades del segon punt separades per una coma: ")
    dist=math.sqrt(((c-a)**2)+((d-b)**2))
    print "El nombre enter que mes se apropa a la distancia euclideana entre aquests punts es el",int(dist)
    print " "

# Programa que representa tots els nombres naturals els factorials dels quals son menor que 62044840173323943936000
def factmenor():
    print "PROGRAMA G"
    print "Aquest programa posa a pantalla tots els nombres naturals els factorials dels quals son menor que 62044840173323943936000"
    x=1
    while math.factorial(x)<62044840173323943936000:
        print x
        x=x+1
    print " "

# Programa que calcula la suma de tots els nombres fins a mil que son divisibles per 3 i 5
# (Que a la vegada ho són també per 15, per tant ens basta amb tractar només amb els nombres de 15 en 15)
def suma():
    print "PROGRAMA H"
    print "Aquest programa posa a pantalla la suma de tots els nombres fins a mil que son divisibles per 3 i 5:"
    suma=0
    for x in range(0,1001,15):
        suma=suma+x
    print suma
    print " "

# Programa que calcula el menor nombre que sigui divisible per 2,3,4,5,6,7,8,9 i 10
# (Que a la vegada simplificat vol dir que és divisible per 5,7,8,9)
def divisible():
    print "PROGRAMA I"
    print "Aquest programa posa a pantalla el menor nombre que sigui divisible per 2,3,4,5,6,7,8,9 i 10:"
    for x in range(1,math.factorial(10)):
        if x%(5*7*8*9)==0:
            print x
            break
    
futval()

convert()

exp()

punts()

euclid()

euclid2()

factmenor()

suma()

divisible()
