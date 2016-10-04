# ALGOR�SMICA: Grupo F
# Ejercicio 6: Algoritmo de Levenshtein en el ADN humano
# Programa de Christian Jos� Soler

import time

def main():

    print "EXERCICI 6 : Aquest programa es una simulacio de l'algorisme de Levenshtein en el ADN huma"
    print ""

# Definimos first, que son la lista de patrones que queremos buscar y su �ndice en la lista, 'o'
    first = ['AGATACATTAGACAATAGAGATGTGGTC','GTCAGTCTGGCCTTGCCATTGGTGCCACCA','TACCGAGAAGCTGGATTACAGCATGTACCATCAT']
    o = 0

# Inicializamos     petit, que ser� la lista de ediciones m�nimas para llegar del substring parecida a cada patr�n
#                   posicion, que ser� la lista de posiciones dentro de la l�nea del substring m�s parecido para cada patr�n
#                   texto, que ser� la lista de substrings m�s parecidos al patr�n para cada patr�n
#                   linea, que ser� la lista con los n�meros de l�nea donde se encuentra

# Ponemos valores ya concretos en lugar de listas vac�as,
    # Porque sabemos que cambiar de valores una lista es menos costoso que llenarla

    petit = [1000]*len(first)
    posicion = [0]*len(first)
    texto = [0]*len(first)
    linea = [0]*len(first)

# Definimos second, que ser� una lista con cada una de las l�neas del archivo HUMAN-DNA.txt y 'a' que es su �ndice en la lista

    archivo = open("HUMAN-DNA.txt","r")
    second = archivo.readlines()
    a = 0

# Decimos que mientras no sobrepasemos el n�mero de patrones
    # Empezamos un reloj para cada patr�n y
    # Con la lista del resultado que obtenemos de ejecutar levenshtein_distance para cada patr�n y l�nea procedemos
    # Definimos el booleano r, que controlar� que dentro del Levenshtein no se hagan c�lculos innecesarios para cada valor
    
    while o < len(first):
        r = False
        t1 = time.clock()
        llista = levenshtein_distance (first, second, a, o, r)

# Con el valor inicial de petit para cada patr�n, encontramos la distancia de edici�n m�nima y mientras cambiamos valores:
    # De la edici�n m�nima, petit
    # De la posici�n, posicion
    # Del substring, texto
    # Del n�mero de l�nea, linea
        
        if llista[0] < petit[o]:
            petit[o] = llista[0]
            linea[o] = a+1   # Sumamos uno porque el programa cuenta a partir del 0
            
# Con este if, controlamos que para cada patr�n se ejecute tantas veces como lineas haya en el fichero

        if a < (len(second)-1):
            a += 1

# Con este if, si se acaban las l�neas para el patr�n
    # Hacemos los c�lculos necesarios con el valor m�nimo para encontrar la posici�n y el substring m�s parecido
    # Acabamos de contar el reloj
    # Imprimimos los resultados de ese patr�n
    # Cambiamos de patr�n e iniciamos de nuevo las l�neas
            
        if a >= (len(second)-1):
            llista2 = levenshtein_distance(first, second, linea[o]-1, o, True)
            posicion[o] = llista2[1] 
            texto[o] = llista2[2]
            t2 = time.clock()
            print "El patro",first[o],"es troba a la linia",linea[o],"posicio",posicion[o],"del cromosoma 2 huma"
            print "La seva distancia de edicio es:",petit[o]
            print "El substring del cromosoma huma mes semblant es:",texto[o]
            print "El temps de calcul ha estat: %0.3f ms" % ((t2-t1)*1000)
            print ""
            o += 1
            a = 0
            

def levenshtein_distance(first, second, a, o, r):

# Definimos la lista resultat, donde haremos que la funcion devuelva
    # Distancia de edici�n m�nima
    # Posici�n del substring m�s parecido
    # Substring m�s parecido
    
    resultat = [1000]*3
    y = 0
    minimo_edicion = 1000

# Hacemos el algoritmo de Levenshtein, que figura en los apuntes de clase
    
    if len(first[o]) > len(second[a]):
        first[o], second[a] = second[a], first[o]
    first_length = len(first[o]) + 1
    second_length = len(second[a]) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length):
        distance_matrix[i][0] = i
    for j in range(second_length):
        distance_matrix[0][j] = 0   # Hago un cambio para que la primera fila sea de ceros

    for i in xrange(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if (first[o])[i-1] != (second[a])[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
            
# Para calcular la distancia de edici�n m�nima hacemos recorrer toda la �ltima fila
    # Miramos si el n�mero de la �ltima fila es m�s peque�a que la distancia minima de edici�n
        # Si lo es, Este se convierte en la distancia de edici�n m�nima
        #           Su posici�n se guarda

    for x in range(second_length):
        if minimo_edicion >= distance_matrix[first_length-1][x]:
            minimo_edicion = distance_matrix[first_length-1][x]
            y = x
    final = y

# Si el booleano r es cierto (solo en caso de distancia de edici�n m�nima):
    # Definimos z, que ser� la longitud del patr�n, es decir first_length-1
    # Aplicamos las reglas de la matriz, pero al rev�s hasta llegar a la posici�n que buscamos

    if r == True:
        z = first_length-1
        while z > 1:
            deletion = distance_matrix[z-1][y]+1
            insertion = distance_matrix[z][y-1]+1
            substitution = distance_matrix[z-1][y-1]
            if (first[o])[z-1] != (second[a])[y-1]:
                substitution += 1
            if substitution <= distance_matrix[z][y]:
                y -= 1
                z -= 1
            elif deletion <= distance_matrix[z][y]:
                z -= 1
            elif insertion <= distance_matrix[z][y]:
                y -=1
        
                
# Para calcular la posici�n en la matriz, hacemos posici�n anteriormente calculada - 1
# Para calcular el subestring hacemos desde la posici�n hasta la posici�n del n�mero m�nimo a la �ltima fila

    posicion_matriz = y-1
    substring = (second[a])[y-1:final]

    resultat[0] = minimo_edicion
    resultat[1] = posicion_matriz+1  # Sumamos uno, porque el programa cuenta a partir del 0
    resultat[2] = substring
    
    return resultat

main()
