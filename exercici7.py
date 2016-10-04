# ALGOR�SMICA: Grupo F
# Ejercicio 7: Dividir y vencer
# Programa de Christian Jos� Soler

def negatius(llista):

# Definim els contadors del quicksort que recorreran la llista

    cont_1 = 0
    cont_2 = len(llista)-1

# Apliquem quicksort per ordenar els elements segons signe, modificant el codi dels apunts de classe

    while cont_2 > cont_1:
        llista[cont_1], llista[cont_2] = llista[cont_2], llista[cont_1]
        while llista[cont_1] < 0:
            cont_1 += 1
        while llista[cont_2] >= 0:
            cont_2 -= 1
            
    print "La llista amb nombres qualificats segons signe �s: ",llista

def exponent(a,n):

# Prenent com a exemple, la successi� recursiva de Fibonacci fem com a sentinella n==0 que �s 1 y n==1 que �s a

    if n == 0:
        return 1
    if n == 1:
        return a
    else:
        
# Per fer la recursi�:
    # Distinguim els casos de quan �s parell i imparell (perqu� per divisi� entera per imparells faltar� un de l'exponent 
        if n % 2 != 0:
            return exponent(a,n/2) * exponent (a,n/2) * a
        else:
            return exponent(a,n/2) * exponent (a,n/2)

def reverse(frase):

# Utilitzem com a exemple, el mergesort,
# Doncs com a sentinella definim que quan la recursi� dividiexi fins a arribar a un element
    # Tornem a unir-los per�, al rev�s
    
    if len(frase) < 2:
        return frase
    else:
        return reverse(frase[(len(frase)/2):]) + reverse(frase[:(len(frase)/2)])

def aprop(conjunt):

# Complexitat: O(n * log n), ja que nom�s fem l'algorisme de mergesort que �s O(n*log n) i despr�s nom�s O(n) operacions
    

# Definim una llista de minims, on guardarem les distancies guardades
# i ordenat que ordenarem amb l'algorisme de mergesort dels apunts de classe, que figura a sota

    minimos = [0] * (len(conjunt)-1)
    ordenat = mergesort(conjunt)

# Emplenem la llista amb els m�nims que trobem amb recursi� 

    for x in range(len(ordenat)-1):
        minimos[x] = distancia_min(ordenat[x], ordenat[x+1])

# Definim un m�nim a l'atzar, el primer, i anem comparant fins a trobar-ne la posici� on s'ubica i fem impressi� de resultats

    minimo = minimos[0]    
    posicio = 0
    for x in range(len(minimos)-2):
        if minimos[x] < minimo:
            minimo = minimos[x]
            posicio = x

    print "Els punts amb distancia minima son", ordenat[posicio],"i",ordenat[posicio+1]


def elimina(lista):

# Ordenem la llista i al tenir-la ordenada nom�s ens hem de fixar si per cada element, l'element seg�ent �s igual a l'anterior
    # Canviem el n�mero per un espai

    ordenat = mergesort(lista)
    for x in range(len(ordenat)-1):
        if ordenat[x] == ordenat[x+1]:
            ordenat[x] = ''
    print ordenat
    
def distancia_min(nombre1, nombre2):

# Aquesta subfunci� de aprop troba la dist�ncia entre dos nombres

    if nombre1 < nombre2:
        return nombre2-nombre1
    else:
        return nombre1-nombre2

def mergesort(lista):
    if len(lista) < 2:
        return lista
    else:
        middle = len(lista) / 2
        left = mergesort(lista[:middle])
        right = mergesort(lista[middle:])
        return merge(left, right, lista)

def merge(left, right, lista):
    result = []
    i ,j = 0, 0
    while(i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
        
    result += left[i:]
    result += right[j:]
    return result
