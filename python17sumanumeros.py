#Pedimos al usuario un texto numérico
# y que nos sume cada caracter del texto y mostrar la suma de cada número/letra
print("Suma números texto string")
print("Introduzca un texto: ")
textoNumeros = input()
suma = 0
longitud = len(textoNumeros)
# recorremos cada letra del texto
for i in range(longitud):
    #almacenamos cada letra de cada posición
    letra = textoNumeros[i]
    #convertimos cada letra a entero
    numero = int(letra)
    #sumamos cada número que tenemos
    suma = suma + numero
print("LA suma de "+ textoNumeros +" es "+ str(suma))
print ("Fin de programa")

