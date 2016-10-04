def cesar():
    frase = raw_input("Digui'm la frase que vol xifrar: ")
    x = list(frase)
    clau = input("Digui'm la clau del xifratge: ")%26
    for x in frase:
        if 64 < ord(x) < 91:
            if ord(x) == 90:
                print chr(64 + clau),
            elif ord(x) + clau > 90:
                y = clau - (90 - ord(x))
                print chr(65 + y),
            else:
                print chr(ord(x)+clau),
        elif 96 < ord(x) < 123:
            if ord(x) == 122:
                print chr(96 + clau),
            elif ord(x)+clau > 122:
                y = clau - (122 - ord(x))
                print chr(97 + y),
            else:
                print chr(ord(x) + clau),
        else:
            print x,            
cesar()
