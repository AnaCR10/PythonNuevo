print("Vamos a crear una lista en Python")
listaNumeros = [12, 56,77,88,1,99,22]
listaNumeros.sort() #ordena la lista de forma ascendente
#si queremos que los ordene de forma descendente
# ponemos reverse = True
listaNumeros.sort(reverse=True)
#realizamos un bucle para mostrar los números actualmente
for i in range(len(listaNumeros)):
    print(listaNumeros[i])
#las listas comienzan en cero y finalizan en len -1
print("Número 0: ", listaNumeros[0])
print("Número 1: ", listaNumeros[1])

#podemos crear listas de cualquier tipo
print("vamos a crear una lista de nombres ")
listaNombres = ["Ana", "Lucas","Adrian", "Diana","Antonia","Lucas"]
print("Nombre 2: ", listaNombres[2])
print("Nombre 4: ", listaNombres[4])
#append crea un nuevo elemento en la lista al final
listaNombres.append ("Lucia")
print("Nombre 5: ", listaNombres[5])
#insert crea un nuevo elemento pero en una posición
listaNombres.insert(4, "Infiltrado")
print("Nombre 4: ", listaNombres[4])
#el método remove elimina un objeto dentro de una lista 
# si hay repetidos solo elimina el primero
# y si no lo encuentra da error, todo depende del lenguaje
#listaNombres.remove("Lucas")
#pop elimina un elemento por su posción
#listaNombres.pop(1)
# con del puedo eliminar un rango, es decir, permite hacer slicing
del listaNombres[0:4]
#vamos a recorrer todos los elementos de la lista y mostrar su posición
for i in range(len(listaNombres)):
    print("Nombre "+str(i)+" = "+listaNombres[i])
#len devuelve el número de elementos de una lista
print(len(listaNombres))
listaNombres.clear()
# print("Diana" in listaNombres)
# print("elementos")
# for i in range(len(listaNombres)):
#     print("Nombre "+str(i)+" = "+listaNombres[i])
listaNombres.sort()
for i in range(len(listaNombres)):
     print("Nombre "+str(i)+" = "+listaNombres[i])