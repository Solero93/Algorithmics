def dni():
    dni = input("Digui el seu numero del DNI (8 caracters): ")
    len_dni = len(str(dni))
    while len_dni != 8:
        dni = input("No es valid, intenti de nou (8 nombres!): ")
        len_dni = len(str(dni))
    lletres = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    lletra = lletres [(dni % 23)]
    print "El seu DNI complert es: ",dni, "-" ,lletra,    
dni()
