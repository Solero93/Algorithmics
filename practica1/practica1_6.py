import math

def euclid2():
    a,b=input ("Posa'm les coordenades del primer punt separades per una coma: ") 
    c,d=input ("Posa'm les coordenades del segon punt separades per una coma: ")
    dist=math.sqrt(((c-a)**2)+((d-b)**2))
    print "El nombre enter que mes s'apropa a la distancia euclideana entre aquests punts es el ",int(dist)
euclid2()
