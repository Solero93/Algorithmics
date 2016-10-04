import math

def aprop(conjunt):
    ordenat = mergesort(conjunt)

def mergesort(conjunt):
    if len(conjunt) < 2:
        return conjunt
    else:
        return merge(conjunt[:(len(conjunt)/2)], conjunt[(len(conjunt)/2):])

def merge(left, right):
    if len(left) == 1:
        return left
    if len(right) == 1:
        return right
    if 

    minimo = math.abs(conjunt[1]-conjunt[0])
    
