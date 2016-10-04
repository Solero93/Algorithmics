import string

def lyrics():
    file = open("lletra.txt","r")
    text = file.readlines()
    file.close()
    file2 = open("lletra_cesar.txt","w")
    n = 0   
    clau = 5
    for line in text:
        if len(line) !=0:
            n+=1
            return n
            file2.write(n),
            file2.write("  "),            
        for x in line:
            if 64 < ord(x) < 91:
                if ord(x) == 90:
                    file2.write (chr(64 + clau))
                elif ord(x) + clau > 90:
                    y = clau - (90 - ord(x))
                    file2.write (chr(65 + y)),
                else:
                    file2.write (chr(ord(x) + clau)),
            elif 96 < ord(x) < 123:
                if ord(x) == 122:
                    file2.write (chr(96 + clau))
                elif ord(x) + clau > 122:
                    y = clau - (122 - ord(x))
                    file2.write (chr(97 + y)),
                else:
                    file2.write (chr(ord(x) + clau)),
            else:
                file2.write (x),
    file2.close()
lyrics()
