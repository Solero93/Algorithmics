# ALGORÍSMICA: Grupo F
# Ejercicio 6: Algoritmo de Levenshtein en el ADN humano
# Programa de Christian José Soler

import time

def main():

    print "EXERCICI 6 : Aquest programa es una simulacio de l'algorisme de Levenshtein en el ADN huma"
    print ""

# Definimos first, que son la lista de patrones que queremos buscar y su índice en la lista, 'o'
    first = ['AGATACATTAGACAATAGAGATGTGGTC','GTCAGTCTGGCCTTGCCATTGGTGCCACCA','TACCGAGAAGCTGGATTACAGCATGTACCATCAT']
    o = 0

# Inicializamos     petit, que será la lista de ediciones mínimas para llegar del substring parecida a cada patrón
#                   posicion, que será la lista de posiciones dentro de la línea del substring más parecido para cada patrón
#                   texto, que será la lista de substrings más parecidos al patrón para cada patrón
#                   linea, que será la lista con los números de línea donde se encuentra

# Ponemos valores ya concretos en lugar de listas vacías,
    # Porque sabemos que cambiar de valores una lista es menos costoso que llenarla

    petit = [1000]*len(first)
    posicion = [0]*len(first)
    texto = [0]*len(first)
    linea = [0]*len(first)

# Definimos second, que será una lista con cada una de las líneas del archivo HUMAN-DNA.txt y 'a' que es su índice en la lista

    archivo = open("HUMAN-DNA.txt","r")
    second = archivo.readlines()
    a = 0

# Decimos que mientras no sobrepasemos el número de patrones
    # Empezamos un reloj para cada patrón y
    # Con la lista del resultado que obtenemos de ejecutar levenshtein_distance para cada patrón y línea procedemos
    # Definimos el booleano r, que controlará que dentro del Levenshtein no se hagan cálculos innecesarios para cada valor
    
    while o < len(first):
        r = False
        t1 = time.clock()
        llista = levenshtein_distance (first, second, a, o, r)

# Con el valor inicial de petit para cada patrón, encontramos la distancia de edición mínima y mientras cambiamos valores:
    # De la edición mínima, petit
    # De la posición, posicion
    # Del substring, texto
    # Del número de línea, linea
        
        if llista[0] < petit[o]:
            petit[o] = llista[0]
            linea[o] = a+1   # Sumamos uno porque el programa cuenta a partir del 0
            
# Con este if, controlamos que para cada patrón se ejecute tantas veces como lineas haya en el fichero

        if a < (len(second)-1):
            a += 1

# Con este if, si se acaban las líneas para el patrón
    # Hacemos los cálculos necesarios con el valor mínimo para encontrar la posición y el substring más parecido
    # Acabamos de contar el reloj
    # Imprimimos los resultados de ese patrón
    # Cambiamos de patrón e iniciamos de nuevo las líneas
            
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
    # Distancia de edición mínima
    # Posición del substring más parecido
    # Substring más parecido
    
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
            
# Para calcular la distancia de edición mínima hacemos recorrer toda la última fila
    # Miramos si el número de la última fila es más pequeña que la distancia minima de edición
        # Si lo es, Este se convierte en la distancia de edición mínima
        #           Su posición se guarda

    for x in range(second_length):
        if minimo_edicion >= distance_matrix[first_length-1][x]:
            minimo_edicion = distance_matrix[first_length-1][x]
            y = x
    final = y

# Si el booleano r es cierto (solo en caso de distancia de edición mínima):
    # Definimos z, que será la longitud del patrón, es decir first_length-1
    # Aplicamos las reglas de la matriz, pero al revés hasta llegar a la posición que buscamos

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
        
                
# Para calcular la posición en la matriz, hacemos posición anteriormente calculada - 1
# Para calcular el subestring hacemos desde la posición hasta la posición del número mínimo a la última fila

    posicion_matriz = y-1
    substring = (second[a])[y-1:final]

    resultat[0] = minimo_edicion
    resultat[1] = posicion_matriz+1  # Sumamos uno, porque el programa cuenta a partir del 0
    resultat[2] = substring
    
    return resultat

main()
