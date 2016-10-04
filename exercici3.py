# EXERCICI 3
# Un programa per manipular variables de tipus string
# Escrit per : Christian José Soler

import string

def acro():
    print "PROGRAMA A: Acronim de una frase"
    # Demanem a l'usuari la frase,
        # A aquesta la separem en paraules separades
    # Fem una espècie de "contador de strings" per ajuntar les primeres lletres
    # I al final imprimim a pantalla la variable acronim en majúscules
    frase = raw_input("Entra la frase el acronim de la qual vols saber: ")    
    x=string.split(frase)
    acronim=""
    for lletra in x:
        acronim=acronim+lletra[0]
    print "El seu acronim es:",acronim.upper()
    print " "

def paraules():
    print "PROGRAMA B: Contador de paraules de una frase"
    # Demanem a l'usuari la frase,
        # A aquesta la separem en paraules separades
    # I imprimim a pantalla la longitud de la separació, ja que l'ordinador la paraula ho contará com un sol string
    frase=raw_input("Entri la frase i conto la quantitat de paraules: ")
    x=frase.split()
    print "La quantitat de paraules de aquesta frase es de:",len(x),"paraules"
    print " "
    
def cesar():
    print "PROGRAMA C: Codificador de una frase"
    # Demanem a l'usuari la frase que vol xifrar i la clau amb la qual ho vol fer,
        # En la clau treballem amb el seu módul amb 26, ja que el procés de codificació és periódic i per cada 26 vegades es repeteix.
    # Apliquem condicions a cada lletra de la frase segons si son lletres majúscules, minúscules o no són cap (en aquest cas només fem print)
        # Dintre de la condició de majúscules i minúscules fem la subcondició de si estem parlant de la z que faci la suma entre el ord(a-1) i la clau
        # Si la ord(lletra)+clau supera el valor de la z,
            # Hem de recórre al cálcul de la diferéncia entre la ord(nova posició) i ord(a), després aquest li sumem a l'ord(a), tenint així la nova lletra
        # I en la resta de casos només ha de fer print al ord(lletra+clau)
    frase = raw_input("Digui'm la frase que vol xifrar: ")
    x = list(frase)
    clau = input("Digui'm la clau del xifratge: ")%26
    for x in frase:
        if 64 < ord(x) < 91:
            if ord(x) == 90:
                print chr(ord(a-1) + clau),
            elif ord(x) + clau > 90:
                y = clau - (90 - ord(x))
                print chr(65 + y),
            else:
                print chr(ord(x)+clau),
        elif 96 < ord(x) < 123:
            if ord(x) == 122:
                print chr(ord(a-1) + clau),
            elif ord(x)+clau > 122:
                y = clau - (122 - ord(x))
                print chr(97 + y),
            else:
                print chr(ord(x) + clau),
        else:
            print x,  
    print " "

def lyrics():
    print "PROGRAMA D: Codificador de la lletra de una canco"
    # Primer li diem al programa que obri l'arxiu lletra.txt en versió per llegir i fem un "import" de la informació que conté
    # Després obrim un altre arxiu, lletra_cesar.txt, en versió per escriure i si no hi és, Python la creará
    # Definim n=0 i clau=5
    # Fem operacions per cada linea del text:
        # Primer per cada linea del text que tingui al menys un carácter li dongui un nombre n (comencant per l'1 i anar augmentant)
        # Després per cada lletra de la línea implementem l'exercici anterior, peró no imprimint a pantalla sinó escrivint en l'altre arxiu lletra_cesar.txt
    file = open("lletra.txt","r")
    text = file.readlines()
    file.close()
    file2 = open("lletra_cesar.txt","a")
    n = 0   
    clau = 5
    for line in text:
        if len(line) !=0:
            n+=1
            return n
            file2.write(n),
            file2.write(" "),
            file2.write(" "),
        for x in line:
            if 64 < ord(x) < 91:
                if ord(x) == 90:
                    file2.write (chr(64 + clau))
                elif ord(x) + clau > 90:
                    y = clau - (90 - ord(x))
                    file2.write (chr(65 + y)),
                else:
                    file2.write (chr(ord(x) + clau)),
            elif 96 < ord(x) < 123:
                if ord(x) == 122:
                    file2.write (chr(96 + clau))
                elif ord(x) + clau > 122:
                    y = clau - (122 - ord(x))
                    file2.write (chr(97 + y)),
                else:
                    file2.write (chr(ord(x) + clau)),
            else:
                file2.write (x),
    file2.close()
    print " "

def sequencia():
    print " "
    print "PROGRAMA E: Contador de lletres h despres de lletres t en una canco"
    # Primer obrim l'arxiu lletra.txt un altre cop
    # Posem al contador a 0 abans de comencar
    # Per a cada linia del text:
        # Si 'th' pertany a la linia en minúscules, el contador augmenta 1
        # El mateix per 't h' (jo he suposat que t seguit per un h també inclou espais entre elles)
    # Fem impressió a pantalla del resultat
    file = open("lletra.txt","r")
    text = file.readlines()
    file.close()
    contador = 0
    for line in text:
        if 'th' in line.lower():
            contador+=1
        elif 't h' in line.lower():
            contador+=1
    print "Hi ha",contador,"vegades una t seguit per h en aquest arxiu de text"
    print " "

def paraula():
    print "PROGRAMA F: Contador de una paraula concreta dins una canco"
    # Primer obrim l'arxiu lletra.txt un altre cop
    # Definim paraula com la paraula que posa l'usuari, peró aquesta és convertida en minúscules després
    # Posem el contador a 0
    # Per a cada linia del text,
        # Si la paraula de l'usuari pertany a la linia en minúscules, fem augmentar el contador amb 1
    # Imprimim a pantalla el resultat
    file = open("lletra.txt","r")
    text = file.readlines()
    file.close()
    paraula = string.lower(raw_input("Posi'm la paraula que vol cercar: "))
    contador = 0
    for line in text:
        if paraula in line.lower():
            contador+=1
    print "Surt",contador,"vegades la paraula",paraula,

acro()

paraules()

cesar()

lyrics()

sequencia()

paraula()
