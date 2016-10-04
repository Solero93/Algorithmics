import math

def funcld(x):
    return x*math.sin(10*(math.pi)*x)+1.0

def funcld_2(x,y):
    return 200-(((x**2)+y-11)**2)-((x+(y**2)-7)**2)

def frangeld(start_x, end_x, inc_x):
    while start_x <= end_x:
        yield start_x
        start_x += inc_x

def frangeld_2(start_x, end_x, inc_x, start_y, end_y, inc_y):
    for i in frangeld(start_x, end_x, inc_x):
        for j in frangeld(start_y, end_y, inc_y):
            yield start_x, start_y
            
def searchld():
    maximo = 0.0
    for i in frangeld(-1,2,0.000001):
        if maximo < funcld(i):
            maximo = funcld(i)
            abscissa = i
    print maximo, abscissa

def searchld_2(start_x, end_x, inc_x, start_y, end_y, inc_y):
    maximo = 0.0
    while lista2[0] != end_x and lista2[1] != end_y:
        lista = frangeld_2(start_x, end_x, inc_x, start_y, end_y, inc_y)
        lista2 = list(lista)
        while 
        if maximo < funcld_2(lista2[0], lista2[1]):
            maximo = funcld_2(lista2[0], lista2[1])
            abscissa = lista2[0]
            ordenada = lista2[1]
    print maximo, abscissa, ordenada
