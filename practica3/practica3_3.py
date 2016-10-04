def nota():
    nota = input ("Digues la teva nota: ")
    quali = ["Suspens", "Aprovat", "Notable", "Excellent", "Matricula"]

    while nota < 0 or nota > 10:
        nota = input ("La teva nota no és válida, intenta de nou: ")
                      
    if nota < 5:
        print "La teva qualificacio es:",quali [0]
    elif nota >= 5 and nota < 7:
        print "La teva qualificacio es:",quali [1]
    elif nota >= 7 and nota < 9:
        print "La teva qualificacio es:",quali [2]
    elif nota >= 9 and nota < 10:
        print "La teva qualificacio es:",quali [3]
    else:
        print "La teva qualificacio es:",quali [4]
    
nota()
