import string

def paraula():
    file = open("lletra.txt","r")
    text = file.readlines()
    file.close()
    paraula = string.lower(raw_input("Posi'm la paraula que vol cercar: "))
    contador = 0
    for line in text:
        if paraula in string.lower(line):
            contador+=1
    print "Surt",contador,"vegades la paraula",paraula,
paraula()
