def negatius(llista):
    cont_1 = 0
    cont_2 = len(llista)-1

    while cont_2 > cont_1:
        llista[cont_1], llista[cont_2] = llista[cont_2], llista[cont_1]
        while llista[cont_1] < 0:
            cont_1 += 1
        while llista[cont_2] >= 0:
            cont_2 -= 1
            
    print llista
