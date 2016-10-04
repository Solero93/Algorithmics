# Ejercicio 9: Búsqueda de los máximos de una función

import math

# Definimos la primera y la segunda función para futuros cálculos

def func1d(x):
    return x*math.sin(10*(math.pi)*x)+1.0

def func2d(x,y):
    return 200-(((x**2)+y-11)**2)-((x+(y**2)-7)**2)

# Definimos las funciones frange1d y frange2d que nos servirá para hacer un range con pasos racionales
    # Con la ayuda de yield

def frange1d(start_x, end_x, inc_x):
    while start_x <= end_x:
        yield start_x
        start_x += inc_x

def frange2d(start_x, end_x, inc_x, start_y, end_y, inc_y):
    for i in frange1d(start_x, end_x, inc_x):
        for j in frange1d(start_y, end_y, inc_y):
            yield i, j
            
# Hacemos la búsqueda del valor máximo por fuerza bruta del máximo:
            
def search1d(start_x, end_x, inc_x):

# Definimos:
    maximo = func1d(start_x)    # Nos servirá para buscar el valor máximo de la función
    punts = [False] * 1000      # Será el vector inicializado donde guardaremos donde se encuentra dicho valor máximo (suponemos que en más sitios)    
    index = 0                   # Índice para poner los valores en dicha lista
    cont_passos = 0             # Contador de cálculos hechos
    
    for i in frange1d(start_x, end_x, inc_x):
        cont_passos += 1

        # Hacemos una búsqueda de los máximos absolutos con esa tolerancia de la función:
            # Si vemos un valor mayor que el "maximo" pues cambiamos de máximo e inicializamos de nuevo la lista de posiciones
            # Si vemos un valor igual que el "maximo" añadimos su posición a la lista de posiciones
        
        if maximo < func1d(i):
            maximo = func1d(i)
            punts = [False] * 1000
            index = 0
        if maximo == func1d(i):
            punts[index] = i
            index += 1

    # Hacemos impresión de los resultados
            
    print "El valor máxim és:",maximo
    print "Es troba a les abscisses:",
    indice2 = 0
    while (punts[indice2] != False):
        print punts[indice2],", ",
        indice2 += 1
    print ""
    print "S'han fet", cont_passos, "cálculs per arribar al resultat."

def search2d(start_x, end_x, inc_x, start_y, end_y, inc_y):

    #Definimos:
    maximo = func2d(start_x, start_y)   # Nos servirá para buscar el valor máximo de la función
    ordenada = [False] * 1000           # Serán vectores inicializado donde guardaremos donde se encuentra dicho valor máximo (suponemos que en más sitios) 
    abscissa = [False] * 1000
    index = 0                           # Índice para poner los valores en dichas listas
    cont_passos = 0                     # Contador de cálculos hechos
    
    for i in frange2d (start_x, end_x, inc_x, start_y, end_y, inc_y):
        x,y = i
        cont_passos += 1

        # Hacemos el mismo proceso que para el search1d, pero para dos coordenadas
        
        if maximo < func2d(x, y):
            maximo = func2d(x, y)
            ordenada = [False] * 1000
            abscissa = [False] * 1000
            index = 0
        if maximo == func2d(x, y):
            ordenada[index] = y
            abscissa[index] = x
            index += 1
            
    print "El valor máxim és:", maximo
    print "Es troba a les coordenades:",
    indice2 = 0
    while ordenada[indice2] != False:
        print "(", abscissa[indice2], ", " , ordenada[indice2] , ") ",
        indice2 += 1
    print ""
    print "S'han fet",cont_passos,"cálculs per arribar al resultat."
