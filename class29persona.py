class Persona:  #la primera letra se suele poner en mayúscula
    nombre = "" #características de una clase
    apellidos = ""
    email = ""
    anionacimiento = 0
    pais = ""

#la clase también puede tener métodos, es opcional que tenga constructor
#el constructor solo sirve para inicializar las variables
    def __init__(self):
        self.pais = "Francia"

    def __str__ (self):
        return self.apellidos + " "+ self.nombre + " "+ self.pais 


#el contenido self, te permite acceder a todas las variables de la clase
    def getNombreCompleto(self): 
        return self.nombre + " " + self.apellidos
    #aquí accedemos al nombre de la class de arriba
    def getEdad(self):
        return 2025 - self.anionacimiento

    def getDescripcion (self, descripcion):
        return self.getNombreCompleto() +" "+ descripcion