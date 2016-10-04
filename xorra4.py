def mergesort(lista):
    if len(lista) < 2:
        return lista
    else:
        middle = len(lista) / 2
        left = mergesort(lista[:middle])
        right = mergesort(lista[middle:])
        return merge(left, right)

def merge(left, right):
    k = len(left)-1
    l = len(right)-1

    if k == 0:
        return right
    if l == 0:
        return left
    if x[1] <= y[1]:
        return x[1] + merge(x[(l+1):], y[k:])
    else:
        return y[1] + merge(x[l:], y[(k+1):])
