def saludar(nombre):
    print("Bienvenido a Python Mr/Mrs " + nombre)

def despedirse(nombre, dia):
    print("Un placer hoy " + dia+ " Mr/Mrs " + nombre)
#lo de arriba no tiene nada que ver con lo de abajo
#solo si yo lo llamo en el programa principal
print("Métodos con parámetros")
name = "Alumno"
dia= "miercoles"
saludar(name)
despedirse(name,dia)
print("Fin de programa")
