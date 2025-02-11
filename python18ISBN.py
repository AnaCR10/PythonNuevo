# print("Comprobación del ISBN")
# print("Por favor, introduce el ISBN")
# isbn = input()
# longitudIsbn = len(isbn)
# suma = 0
# if (len(isbn)< 10) or (len(isbn)>10 ):
#     print("El isbn introducido no es correcto")
# else:
#     #descomponemos el número del isbn
    
#     for i in range(longitudIsbn):
#     #almacenamos cada número del isbn en una cada posición
#         numero = isbn[i]
#     #multiplcamos cada número por i (que va del 1 al 10)
#         multiplicacion = numero * i
#         producto = int(multiplicacion)
#         print("el resultado de la multiplicación es ", multiplicacion)
#     #tenemos que sumar todas las multiplicaciones y después dividirlo por 11
#     # si el resultado es entero es correcto sino es incorrecto
#         suma = suma + producto

#SOLUCIÓN DEL PROFESOR
print("Validar ISBN")
print("Introduzca un ISBN válido")
isbn= input()
longitud = len(isbn)
if(longitud !=10):
    print("El número no es correcto, debe tener 10 caracteres")
elif (isbn.isdigit() == False):
    print ("El número ISBN debe contener solo números")
else:
    suma = 0
    for i in range(longitud):
        letra = isbn[i]
        numero = int(letra)
        #debemos de coger cada letra y multiplicarla por su posición
        operacion = numero * (i+1)
        suma = suma + operacion
    if (suma % 11 == 0):
        print("el número isbn" + isbn + " es Correcto")
    else:
        print("El número ISBN NO ES CORRECTO")
print("Fin del programa")
    

   
