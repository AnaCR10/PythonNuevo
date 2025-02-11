print("Validación de la dirección de email")
print("Introduzca su dirección de email")
email = input()
#print(email.find("@"))
if (email.startswith("@")or email.endswith("@")):
    print("La dirección de email no es válida, no puede empezar o terminar por @")
elif( email.find("@")!= -1 and email.find(".") !=-1):
    print("La dirección de email tiene al menos una @ y un punto")
    if(email.find(".") > email.find("@")):
        longExtension = email.find (".") + 3
        if(longExtension >3):
            print("La extensión debe tener una longitud menor, revisa el email")
        else:
            print("La extensión es correcta")
        

   
   
    #duda, cómo sé si tiene más de una @
    #vamos a ver la posición de la @ para ver si hay un punto después de ella
    # la pongo en comentarios porque solo lo puedo usar dentro del if posicionArroba = email.find("@")
elif(email.find(".")!= -1):
    print("El mail tiene al menos un punto antes de la extensión, revisa el email")
else:
    
        #vamos a suponer que no puede haber puntos antes de la @
        print("No puede tener una extensión antes de la @")
#vamos a ver que después del punto tiene que haber entre 2 y 3 caracteres





