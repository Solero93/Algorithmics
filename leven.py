def levenshtein_distance():

    first = ['AGATACATTAGACAATAGAGATGTGGTC','GTCAGTCTGGCCTTGCCATTGGTGCCACCA', 'TACCGAGAAGCTGGATTACAGCATGTACCATCAT']
    archivo = open("HUMAN-DNA.txt","r")
    contador = 0
    a = 0
    o = 0
    second = archivo.readlines()
    contador = len(second)
    
    while o < 3:
        print a
        print o
        print contador
        if len(first[o]) > len(second[a]):
            first[o], second[a] = second[a], first[o]
        if len(second[a]) == 0:
            return len(first[o])
        first_length = len(first[o]) + 1
        second_length = len(second[a]) + 1
        distance_matrix = [[0] * second_length for x in range(first_length)]
        for i in range(first_length):
            distance_matrix[i][0] = i
        for j in range(second_length):
            distance_matrix[0][j] = 0

        for i in xrange(1, first_length):
            for j in range(1, second_length):
                deletion = distance_matrix[i-1][j] + 1
                insertion = distance_matrix[i][j-1] + 1
                substitution = distance_matrix[i-1][j-1]
                if first[o][i-1] != second[o][j-1]:
                    substitution += 1
                distance_matrix[i][j] = min(insertion, deletion, substitution)
        print distance_matrix[first_length-1][second_length-1]
                    
        if a <= contador:
            a+=1
        else:
            o+=1
            a=0
    
levenshtein_distance()
