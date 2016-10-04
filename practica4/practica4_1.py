def fib1(n1,n2):
    print n1,n2,
    contador=0
    while contador!=10 :
        n1=n1+n2
        n2=n1+n2
        print n1,n2,
        contador+=1
    
fib1(n1,n2)
