# Un programa per pasar de graus Celsius a Fahrenheit
# Escrit per : Aqu� el vostre nom.
def convert():
    print "Taula de Conversi� de Celsius a Fahrenheit"
    for x in range(1,11):
        celsius=x
        fahrenheit=9.0/5.0*celsius+32
        print repr(celsius),"C ", repr(fahrenheit),"F "
convert()
