import math

def punts():
    a,b=input ("Posa'm les coordenades del primer punt separades per una coma: ") 
    c,d=input ("Posa'm les coordenades del segon punt separades per una coma: ")
    pendent=float((d-c)/(b-a))
    print "El pendent de la recta que defineixen �s de: ",pendent," unitats"
punts()
