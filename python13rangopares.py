print("Introduce un número de inicio")
inicio = int(input())
print("introduce un número de fin")
fin = int(input())
#realizamos un buble desde un inicio hasta un final +1
for i in range (inicio, fin + 1):
    #aquí preguntamos si el número es par
    if (i % 2 == 0):
        print (i)
print("Fin del programa")

