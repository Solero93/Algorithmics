import string

def otan():
    text = raw_input ("Posi el text que vols convertir al diccionari de la OTAN: ")
    diccionari = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel", "I":"India", "J":"Juliet", "K":"Kilo", "L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango", "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"Xray", "Y":"Yankee", "Z":"Zulu"}
    print "El text convertit queda de la seguent forma: "
    for x in string.lower(text):
        if ord(x) > 96 and ord(x) < 123:
            y = string.upper(x)
            nato = diccionari[y]
            print nato,
        else:
            print x,
otan()
