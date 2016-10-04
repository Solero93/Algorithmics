import string

def paraules():
    frase=raw_input("Entri la frase i conto la quantitat de paraules: ")
    x=string.split(frase)
    print len(x)
paraules()    
