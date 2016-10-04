import random

def llista():
    paraules = raw_input("Posi una frase per desordenar: ")
    llista = list(paraules)
    random.shuffle(llista)
    llista2 = "".join(llista)
    print "La frase desordenada queda:",llista2
llista()
