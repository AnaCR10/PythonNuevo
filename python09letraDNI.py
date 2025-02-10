print("Introduce tu DNI sin letra")
dni = int(input())
dni_letra= dni-int(dni/23)*23
# otra forma de calcularlo
# dni_letra =dni % 23
print(dni_letra)

#vamos a poner la tabla con las letras
if(dni_letra == 0):
    print("T")
elif( dni_letra == 1):
    print("R")
elif( dni_letra == 2):
    print("W")
elif( dni_letra == 3):
    print("A")
elif( dni_letra == 4):
    print("G")
elif( dni_letra == 5):
    print("M")
elif( dni_letra == 6):
    print("Y")
elif( dni_letra == 7):
    print("F")
elif( dni_letra == 8):
    print("P")
elif( dni_letra == 9):
    print("D")
elif( dni_letra == 10):
    print("X")
elif( dni_letra == 11):
    print("B")
elif( dni_letra == 12):
    print("N")
elif( dni_letra == 13):
    print("J")
elif( dni_letra == 14):
    print("Z")
elif( dni_letra == 15):
    print("S")
elif( dni_letra == 16):
    print("Q")
elif( dni_letra == 17):
    print("V")
elif( dni_letra == 18):
    print("H")
elif( dni_letra == 19):
    print("L")
elif( dni_letra == 20):
    print("C")
elif( dni_letra == 21):
    print("K")
elif( dni_letra == 22):
    print("E")
elif( dni_letra == 23):
    print("T")


