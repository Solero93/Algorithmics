import string

def sequencia():
    file = open("lletra.txt","r")
    text = file.readlines()
    file.close()
    contador = 0
    for line in text:
        if 'th' in line.lower():
            contador+=1
        elif 't h' in line.lower():
            contador+=1
    print contador
sequencia()
