import string
def lyrics():
    file = open("lletra.txt","r")
    text = file.readlines()
    len(text)
    file.close()
    file = open("lletra_cesar.txt","a")
    n=5
    for line in text:
        for x in line:
            x= string.lower(x)
            num = ord(x)
            if num > 96 and num <= 122 :
                    num = num + n
                    if num>122:
                        num=num-122+96
                        message = ''
                        message = message + chr(num)
                        
                        file.write (message)
                        
                        
                    else:
                        num = ord(x)
                        num = num + n
                        message = ''
                        message = message + chr(num)
                       
                        file.write (message)
            else :
                    num = ord(x)
                    message =''
                    message= chr(num)
                    
                    file.write(message)
    file.close()

    
    inp = open("lletra_cesar.txt","r")
    text = inp.readlines()
    inp.close()
    ind = (0)
    arch = open ("lletra_cesar.txt", "w")
    for line in text:
        
        ind+=1
        

        
        
        ind= str(ind)
        
        arch.writelines (ind)
        arch.write(" ")
        arch.write(line)
        
        ind= int(ind)
        
    arch.close()
lyrics()


    
