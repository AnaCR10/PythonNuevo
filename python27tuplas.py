print("Tuplas de Python")
#las tuplas no se pueden modificar, son estáticas
productos = ("Leche", "Cacao", "Avellanas", "Azúcar")
#len da el número de elementos de la tupla
numeroElementos = len(productos) 
# productos[2]="Havenllambas" --- daría error, no se puede incluir nada
#tampoco funcionaria .sort, ya que no se puede cambiar los elementos
#print("Elementos tupla: ", numeroElementos)
for producto in productos:
    print(producto)

