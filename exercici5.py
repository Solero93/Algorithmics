# ALGORÍSMICA, GRUP F
# EXERCICI 5 : Un programa per utilitzar els conceptes de Algorísmes Numérics
# Escrit per : Christian José Soler

import math
import time

# Creem una funció main, des de on s'executaran totes les parts del programa
    # Així resolent el problema entre era1 i era2 perqué són quasibé els mateixos programes peró per valors diferents

def main():
    print "PROGRAMA A: Sequencia de Fibonacci fins un terme n"
    fib1()
    print ""
    print "PROGRAMA B: Maxim comu divisor de dos nombres"
    mcd()
    print ""
    print "PROGRAMA C: Metode de Eratostenes per un nombre n demanat per lusuari"
    era1(n = input("Diguim un numero i calculo els primers fins a aquest: "))
    print ""
    print "PROGRAMA D: Calcul de temps pel Metode de Eratostenes per 10.000"
    era2()
    print ""
    print "PROGRAMA E: Calcul dels factors de un nombre enter demanat per el usuari"
    factorp()
    print ""
    print "PROGRAMA F: Determinacio de si un nombre demanat per el usuari es primer pel Metode de Fermat"
    fermatp()

def fib1():

# Demanem a l'usuari un nombre qualsevol, inicialitzem els rellotges, i fem una crida a fibonacci() amb el valor que ha donat l'usuari
    
    x = input("Digam un nombre enter qualsevol i et calculo a quin numero de la Successio de Fibonacci correspon: ")
    t1 = time.clock()
    print "El nombre correspon a:",fibonacci(x)
    t2 = time.clock()
    print "Ha trigat %0.3f ms en calcular-ho" % ((t2-t1)*1000)
    
def fibonacci(x):

# Comencem la recursió segons l'aprés a classe
    # Si l'usuari ha posat 0, retornem 0 i si ha posat 1, retornem 1
    # En la resta de casos, fem una crida de nou, peró fent sumes amb els dos nombres anterior, fins arribar a tenir 0 o 1 de nou.
# Retornem el resultat a la funció anterior i ho imprimim per l'usuari

    if x == 0: 
        return 0
    if x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

def mcd():

# Demanem a l'usuari dos nombres per estudiar
    
    n = input("Diguim el primer nombre: ")
    m = input("Diguim el segon nombre: ")

# Definim que mentre el segon nombre no s'anulli intercanviem 
    # n per m
    # m pel residu entre n i m
# Finalment fem print del mcd
    
    while m != 0:
        n,m=m,n%m
    print "El seu maxim comu divisor es:",n

def era1(n):

# Definim m=1, que será el nostre primer nombre per estudiar en el bucle
# Definim un contador=0 que ens servirá pel programa era2, perqué haurem de veure com de rápid conta els nombres primers fins a 10.000.000 el programa
# Creem la llista_a que va des del número 2, fins el nombre demanat que direm n

    m = 2
    contador = 0
    llista_a = range(2,n+1)

# La condició d'aquest algorisme és:

    # Mentre la m, sigui més petita a l'arrel quadrada (després definim una variable k, que controlará els múltiples de n, per treure'ls de la llista)
        # Mentre els múltiples de m siguin més petits o iguals a n i a més estiguin dins la llista_a:
            # S'augmenti contador i els múltiples de m (exceptuant m, és clar) es treuen de la llista_a
            
        # Al final del primer bucle augmentem m (controlem els primers)
        # Al final del segon bucle augmentem k (controlem els múltiples dels primers)
        
    # Al acabar imprimim la llista_a
        
    while m < (math.sqrt(n)):
        k = 2
        while m*k <= n:
            s = m*k
            if s in llista_a:
                contador+=1
                llista_a.remove(s)
            k+=1
        m+=1
        
    print "Els primers fins a aquest nombre son: ",llista_a
    print "Hi ha",contador,"primers fins a aquest nombre"

def era2():

# Inicialitzem el rellotge, i establim que es faci el era1 pel valor 1.000.000, perqué per 10.000.000 el programa no pot generar la llista de nombres
    # Quan acabi fem print del temps que s'ha trigat en fer

    t1 = time.clock()
    era1 (n = 1000000)
    t2 = time.clock()
    print "Ha trigat %0.3f ms en calcular-ho" % ((t2-t1)*1000)

def factorp():

# Demanem un nombre qualsevol a l'usuari i inicialitzem el rellotge
    # Establim m=2, que seria el primer factor per comprovar

    n = input ("Diguim un nombre enter qualsevol per factoritzar: ")
    t1 = time.clock()    
    m = 2

# La nostra condició será que mentre el nombre n, sigui divisible per m, m és un factor i hem d'anar comprovant fins que no ho sigui
    # En cas de que no ho sigui, seguim amb un m següent (m+=1)
    # A més, com a condició per finalitzar, si n/m (divisió entera, és clar) és 0, vol dir que no queden més factors de n, i hem de finalitzar el bucle

    print "La seva factoritzacio es: "
    while n != 0:
        if n % m == 0:
            n/=m
            print m," ",
            if n/m == 0:
                break
        else:
            m+=1

# Al final, fem un print del que ha trigat el programa

    t2 = time.clock()
    print ""
    print "Ha trigat %0.3f ms" % ((t2-t1)*1000)

def fermatp():

# Demanem un nombre qualsevol a l'usuari i inicialitzem el rellotge
    # Definim a=2, b=3, c=5 que serán els nostres nombres per aplicar el métode de Fermat
    
    n = input("Diguim un nombre qualsevol i determino si es primer: ")
    t1 = time.clock()
    a=2
    b=3
    c=5

# Com el métode de Fermat consisteix en comprovar si el módul d'uns nombres primers a l'atzar elevats a n-1 donen 1, fem la condició directament
    # Prenem com a excepció, al 2,3,5 que ja sabem que són primers, i per ells el métode no funciona

    if (n==a or n==b or n==c) or ((a**(n-1))%n==1 and (b**(n-1))%n==1 and (c**(n-1))%n==1):
        print "Es primer"
    else:
        print "No ho es"

# Fem print per quan ha trigat el programa en calcular-ho

    t2 = time.clock()
    print "Ha trigat %0.3f ms en calcular-ho" % ((t2-t1)*1000)

main()
