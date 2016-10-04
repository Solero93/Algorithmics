# ALGORÍSMICA, GRUP F
# EXERCICI 4 : Un programa per aprendre a utilitzar coleccions

import string
import random

def mentre():
    print "PROGRAMA A"
    
    # Demanem a l'usuari el nombre natural per treballar i establim els variables inicials pels contadors

    n = input("Digui un nombre natural: ")
    m = 1
    m2 = 1
    contador = 0
    contador2 = 0 
    contador3 = 0
    
    # En la primera part, fem la suma amb la combinació de dos contadors (un que faci la suma i l'altre que marqui limit de la suma fins n)

    while m <= n:
        contador+=m
        m+=1
    print "La suma dels termes fins a aquest nombre es:",contador

    # En la segona part, fem la suma amb la combinació de dos contadors també (un que faci la suma dels imparells i l'altre que marqui limit de la suma fins n)

    while m2 <= n:
        contador2+=m2
        m2+=2
    print "La suma dels termes imparells fins a aquest nombre es:",contador2
    print " "

    # En la tercera part, fem la suma només amb un contador i establim amb un while que fins que x sigui diferent de 999 vagi sumant el programa

    x = input("Digui els nombres seguits per un intro que vol sumar i si ha acabat, posi 999:  ")
    while x != 999:
        contador3+=x
        x = input("Digui els nombres seguits per un intro que vol sumar i si ha acabat, posi 999:  ")
    print "La seva suma és:",contador3
    print " "
    
def inversio():

    print "PROGRAMA B"

    # Demanem a l'usuari la inversió i l'interés amb la qual treballar

    # Mentrestant, definim la constant inversio2, que és el doble de la inversio inicial i el contador de anys = 0

    inversio = input("Digui la inversio amb la qual es vol treballar: ")
    inversio2 = 2*inversio
    interes = input("Digui el interes (exemple: 0.12) : ")
    anys = 0
    
    # Definim que mentres la inversio sigui menor al doble de la inversio inicial,
        # Calculi el nou valor de interés al passar un any i que augmenti el contador de l'any

    while inversio <= inversio2:
        inversio = inversio * (1+interes)
        anys+=1

    print "La seva inversio es duplicara en:",anys,"anys"
    print " "


def nota():

    print "PROGRAMA C"

    # Demanem a l'usuari la seva nota i definim la coleccio de les qualificacions
    
    nota = input ("Digui la seva nota: ")
    quali = ["Suspens", "Aprovat", "Notable", "Excellent", "Matricula"]

    # Excloim les possibilitats de tenir nota sota 0 o sobre 10 amb un while on diem a l'usuari que intenti de nou posar la nota

    while nota < 0 or nota > 10:
        nota = input ("La seva nota no es valida, intenti de nou: ")
                      
    # Definim els intervals de qualificacio amb els seus prints corresponents

    if nota < 5:
        print "La seva qualificacio es:",quali [0]
    elif nota >= 5 and nota < 7:
        print "La seva qualificacio es:",quali [1]
    elif nota >= 7 and nota < 9:
        print "La seva qualificacio es:",quali [2]
    elif nota >= 9 and nota < 10:
        print "La seva qualificacio es:",quali [3]
    else:
        print "La seva qualificacio es:",quali [4]
    print " "
    

def dni():

    print "PROGRAMA D"

    # Demanem a l'usuari el seu numero del DNI

    dni = input("Digui el seu numero del DNI (8 caracters): ")

    # Excloim la possibilitat de que posi un DNI amb més de 8 carácters amb un while, igual que a l'exercici anterior

    len_dni = len(str(dni))
    while len_dni != 8:
        dni = input("No es valid, intenti de nou (8 nombres!): ")
        len_dni = len(str(dni))

    # Definim la coleccio de lletres del DNI i amb el residu de 23 amb el numero del DNI donem la posicio de la coleccio, així trobant la lletra que falta
    
    lletres = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    lletra = lletres [(dni % 23)]
    print "El seu DNI complert es: ",dni, "-" ,lletra,    
    print " "
    

def llista():
    
    print " "
    print "PROGRAMA E"

    # Demanem a l'usuari que posi una frase per desordenar i a aquesta ho separem en una llista de lletres

    # Amb la funcio random.shuffle desordenem les lletres

    # Les tornem a unir amb la funcio string.join

    paraules = raw_input("Posi una frase per desordenar: ")
    llista = list(paraules)
    random.shuffle(llista)
    llista2 = "".join(llista)
    print "La frase desordenada queda:",llista2
    print " "
    

def otan():

    print "PROGRAMA F"

    # Demanem a l'usuari la frase que volem treballar i definim el diccionari de les lletres de la OTAN
    
    text = raw_input ("Posi el text que vol convertir al diccionari fonetic de la OTAN: ")
    diccionari = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel", "I":"India", "J":"Juliet", "K":"Kilo", "L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango", "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"Xray", "Y":"Yankee", "Z":"Zulu"}

    # Fem que per tota x que pertanyi a la frase en minúscules,
        # Si aquesta x és una lletra de l'alfabet anglés:
            # Fem la x en majúscules i assignem la paraula que li correspon al diccionari fonétic de la OTAN i fem print d'aquest
        # Si no ho és, només fem un print, així evitant collapses del programa

    print "El text convertit queda de la seguent forma: "
    for x in string.lower(text):
        if ord(x) > 96 and ord(x) < 123:
            y = string.upper(x)
            nato = diccionari[y]
            print nato,
        else:
            print x,

mentre()

inversio()

nota()

dni()

llista()

otan()
