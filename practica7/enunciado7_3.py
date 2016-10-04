def reverse(frase):
    if len(frase) < 2:
        return frase
    else:
        return reverse(frase[(len(frase)/2):]) + reverse(frase[:(len(frase)/2)])
