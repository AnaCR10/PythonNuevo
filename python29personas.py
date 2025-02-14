#primero importamos la clase persona
from class29persona import Persona
print("Prueba clase Persona")
#creamos una nueva persona
person = Persona()
print(person.pais) #si lo ejecutamos saldrá Francia
person.pais = "España"
person.anionacimiento = 2000
person.email = "email@email.com"
person.nombre ="Alumno"
person.apellidos = "Python"
print(person.getNombreCompleto())
print("Edad: ", person.getEdad())
person2 = Persona()
print(person2.pais)
print(person)
print(person.getDescripcion("Hola caracola"))