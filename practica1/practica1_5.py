import math

def euclid():
    a,b=input ("Posa'm les coordenades del primer punt separades per una coma: ") 
    c,d=input ("Posa'm les coordenades del segon punt separades per una coma: ")
    dist=math.sqrt(((c-a)**2)+((d-b)**2))
    print "La dist�ncia entre aquests punts �s de: ",dist," unitats"
euclid()
