import string

def acro():
    frase=raw_input("Entra la frase l'acronim de la qual vols saber: ")
    x=string.split(frase)
    acronim=""
    for lletra in x:
        acronim=acronim+lletra[0]
    print string.upper(acronim)
acro()
