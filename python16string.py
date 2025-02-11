print("Clase string y funciones")
texto = "primero python" #variable a la que vamos a aplicar los métodos

#vamos probando métodos y viendo qué devuelve

print("upper, ",texto.upper()) #aplicamos el método upper al objeto texto
print("replace, "+ texto.replace("o", "@"))
print("Letra 0: " + texto [0])
print ("longitud, ", len(texto))
print("find P: ", texto.find("t"))
print("find P: ", texto.find("z")) #no hay z en el texto
#vamos a utilizar la SOBRECARGA DE FIND (contenido a buscar, índice) desde el íncide inclusive
print ("fin p sobrecarga ", texto.find("p", 1)) 
print ("rfin p sobrecarga ", texto.rfind("p")) 
print("startswith A", texto.startswith("A"))
print("endswith A", texto.endswith("A"))
print("isdigit() ", texto.isdigit()) # solo es aplicable a dígitos, no negativos
print("isalpha() ", texto.isalpha())
print("isalnum() ", texto.isalnum())
#vamos a ver qué pasa con SLICING (o lo que es lo mismo subcadenas)
#queremos recuperar desde la posición 2 en adelante
print("Posición 2 en adelante ", texto[2:])
#en python podemos recuperar una subcadena
#desde una posición (2) a otra posición (5)
subtexto = texto [2:5]
print("texto[2:5], ", subtexto)
#podemos recorrer cada caracter de un texto
longitud = len(texto)
for i in range(longitud):
    letra = texto[i]
    print("Posición " +str(i) + ":" + letra)
#vamos a comprobar si el usuario ha escrito un nº o no
print("Introduzca un número")
#primero hago una variable auxiliar
aux = input()
#ahora ya puedo preguntarle usando un método
if (aux.isdigit()):
    print("Esto es un numero")
else:
    print("No me has dado un número")
print("Fin del programa")

