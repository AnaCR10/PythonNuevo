def convertirMayusculas (texto):
    return texto.upper()

def convertirMinusculas (texto):
    return texto.lower()

def concatenar (texto1, texto2):
    resultado = texto1 + " " +texto2
    return resultado

def mostrarMenu():
    print("Seleccione una opción")
    print("1.- Convertir mayúsculas")
    print("2.- Convertir minúsculas")
    print("3.- Concatenar textos")
    print("4.- Salir")

#ya tenemos todos los métodos, vamos al programa principal

print("Método Return")
print("Introduzca un texto")
valor = input()
mostrarMenu()
opcion = int(input())
while (opcion != 4):
    resultado = "" #tengo que declarar la variable en la que va a guardar el resultado de la opción elegida
if (opcion == 1):
    resultado = convertirMayusculas(valor) #hay que ponerle una variable para que guarde el resultado de la funión
elif (opcion == 2):
    resultado = convertirMinusculas(valor)
else:
    print("ponga otro texto para concatenar")
    otro = input()
    resultado = concatenar (valor, otro)
print (resultado)

print("Fin de programa")
