print("Conjetura de Collatz")
print("Introduzca un número")
numero = int(input())
#mientras que nuestro numero sea distinto de uno tiene que hacer los cálculos
while (numero != 1):
    #vamos a ver si el numero es par o impar
    if(numero % 2 == 0):
        numero = int(numero / 2)
    else:
        numero = numero * 3 + 1
    print (numero)
print("Fin de programa")

