def elimina(lista):
    ordenat = mergesort(lista)
    for x in range(len(ordenat)-1):
        if ordenat[x] == ordenat[x+1]:
            ordenat[x] = ''
    print ordenat

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
