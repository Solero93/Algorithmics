import string

def lyrics(): 
     file = open("lletra.txt","r")
     text = file.readlines()
     file.close()
     encoding = open("lletra_cesar.txt","w")
     encode= ' '
     num=0
     for line in text:
          for letra in line:
               a = ord(letra)
               k = a + 5
               if 65<=a<=90:
                    if k>90:
                         k= k-26                       
                    elif 39<=k<=64:
                         k= k+26                   
               elif 97<=a<=122:
                    if k>122:
                         k=k-26 
                    elif 70<=k<=96:
                         k=k+26     
               else:
                    a>122 and 96>=a>=91 and 64>=a>=0
                    k=a
               c= str(k)
               for b in c.split ():
                    B = eval (b)
                    encode= encode +chr(B)
          encoding.write(encode)
          break
     encoding.close ()

lyrics()
