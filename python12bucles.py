print("ejemplos de bucles")
print("bucle FOR")
#normalmente las variables de los bucles contadores 
#se representan con una sola letra (i, z, j)
for i in range(5):
    print("valor de i, ", i)

#también le podemos poner un unicio (1) y un fin (6)
for i in range(1,6):
    print("valor de i, ",i)

print("WHILE")
#simpre necesitamos una variable para la condición del bucle
contador = 0
while (contador <= 5):
    #print("Bucle infinito")
    #tenemos que hgacer que salga el bucle
    contador = contador + 1
    print ("contador, ", contador)
print("Fin del programa")