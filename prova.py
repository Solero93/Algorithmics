# Examen de algor�smica


# Tengo el error de que el programa imprime al principio de todo, el valor del coseno directamente, y no encuentro el porqu�
    # Pero soy consciente de ello

    

import string
import math

def phrase2numbers():

# Definimos que para todo car�cter en la frase en min�sculas:
    # Si es una letra que sea impresa a pantalla

    print "Programa Parte 1: Separar frase en letras y n�meros"
    print "La frase separada quedo: "
    
    for x in string.lower(phase):
        if ord(x)>96 and ord(x)<123:
            print x,
    print ""

# Hacemos el mismo for de antes, pero para el resto de car�cteres
    # Nos saldr� en l�nea separada, ya que anteriormente hab�amos hecho un print de ""
    # Pues este programa sirve tanto para n�meros como otros car�cteres especiales

    for x in string.lower(phase):
        if ord(x)<97 or ord(x)>122:
            print x,
    print " "
    print " "
    
def compute_cos():

    print "Programa Parte 2: Coseno de un �ngulo"

# Mientras evaluamos numbers:

# Por la reglas de matem�ticas un �ngulo en grados se convierte a radianos multiplic�ndolo por pi i dividi�ndolo por 180

    rad_angulo = (math.pi)*eval(numbers)/180

# Ya que tenemos el �ngulo en radianes podemos proceder a calcular el coseno del �ngulo

    cos_angulo = math.cos(rad_angulo)
    print "El valor del coseno es: ", cos_angulo
    return cos_angulo

def write_angle():

# Creamos un archivo angulo.txt en formato de escritura para poner el numero cos_numbers_rad

    file = open("angulo.txt","w")
    file.write("El coseno del �ngulo es: ")
    file.write(str(cos_numbers_rad))

phase = 'angulo45grados'

# Al tener el primer programa de la forma que s�lo imprime a pantalla las letras y n�meros separadamente
    # Tengo que poner el valor del n�mero yo mismo
    
numbers = '45'
cos_numbers_rad = compute_cos()

phrase2numbers()

compute_cos()

write_angle()
