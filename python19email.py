# print("Validación de la dirección de email")
# print("Introduzca su dirección de email")
# email = input()
# #print(email.find("@"))
# if (email.startswith("@")or email.endswith("@")):
#     print("La dirección de email no es válida, no puede empezar o terminar por @")
# elif( email.find("@")!= -1 and email.find(".") !=-1):
#     print("La dirección de email tiene al menos una @ y un punto")
#     if(email.find(".") > email.find("@")):
#         longExtension = email.find (".") + 3
#         if(longExtension >3):
#             print("La extensión debe tener una longitud menor, revisa el email")
#         else:
#             print("La extensión es correcta")
        

   
   
#     #duda, cómo sé si tiene más de una @
#     #vamos a ver la posición de la @ para ver si hay un punto después de ella
#     # la pongo en comentarios porque solo lo puedo usar dentro del if posicionArroba = email.find("@")
# elif(email.find(".")!= -1):
#     print("El mail tiene al menos un punto antes de la extensión, revisa el email")
# else:
    
#         #vamos a suponer que no puede haber puntos antes de la @
#         print("No puede tener una extensión antes de la @")
# #vamos a ver que después del punto tiene que haber entre 2 y 3 caracteres



#SOLUCIÓN DEL PROFESORES
print("Validación de email ")
print("Introduzca una dirección de email")
email = input()
#que el email tenga @ 
if (email.find("@")== -1):
    #otra forma if (email.count("@")== 0)
    print("Email sin @")
#que exista un punto
elif(email.find(".") == -1): #también se puede hacer con count
    print("Email sin punto")
# @ ni al ppio ni al final
elif (email.startswith("@")== True or email.endswith("@")== True):
    print("@ al principio o al final del email")
#punto ni al inicio ni al final, lo hacemos de otra forma
elif(email[0] == "." or email.endswith(".") == True):
    print(". al princio o al final")
#que el email solo tenga una @     
# se puede hacer de varias formas, count para ver si hay una arroba
# buscando desde inicio y desde el final para ver si se encuentran,
# # o buscar desde ek inicio y desde ahí a ver si encuentra alguna más
elif(email.count("@")>1):
    print("existe más de una @")
#que exista un punto después de una @
elif(email.find( "@")> email.rfind(".")): #rfind busca desde el final
    print("Debe existir un punto después de la @")
else:
    #necesitamos recuperar el dominio (.com o .es)
    #buscamos la posición del último punto
    ultimoPunto = email.rfind(".")
    #recuperamos el dominio a partir del último punto en adelante
    dominio = email[ultimoPunto + 1:]
    longitudDominio = len(dominio) 
    #ahora comprobamos si la longitud es de 2 a 3 caracteres
    if(longitudDominio >= 2 and longitudDominio <=3):
        print("La extensión del email es correcta")
        print("Email correcto, ", email)
    else:
        print("El email debe tener un dominio de 2 o 3 caracteres")
print("Fin del programa")




