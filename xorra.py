import math

def aprop(conjunt):
    minimos = [0] * (len(conjunt)-1)
    ordenat = mergesort(conjunt)
    
    for x in range(len(ordenat)-1):
        minimos[x] = distancia_min(ordenat[x], ordenat[x+1])

    minimo = minimos[0]    
    posicio = 0
    for x in range(len(minimos)-2):
        if minimos[x] < minimo:
            minimo = minimos[x]
            posicio = x

    print "Els punts amb distancia minima son", ordenat[posicio],"i",ordenat[posicio+1]
    
def distancia_min(nombre1, nombre2):
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
        return merge(left, right)

def merge(left, right):
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
