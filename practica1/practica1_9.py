import math
def divisible():
    for x in range(1,math.factorial(10)):
        if x%(8*9*5*7)==0:
            print x
            break
divisible()
