from class30coche import Coche

#Realizamos la herencia, por eso hacemos el from...
class Deportivo(Coche):
    def getVelocidadMaxima(self):
        #deportivo corre 100 más de un coche
        velocidadCoche = super().getVelocidadMaxima() #super() está cogiendo del que hereda
        return velocidadCoche + 100
        #return super().getVelocidadMaxima()

    def turbo(self):
        self.velocidad +=80
        print("Activando turbo!!!"+ str(self.velocidad))
    def acelerar(self):
        self.velocidad += 60
        print("Acelerando " + self.marca + " a "+ str(self.velocidad)+ " km/h")
        #return super().acelerar() #no sé por qué me sale esto

supercoche = Deportivo()
supercoche.marca ="Ferrari"
supercoche.model = "F40"
supercoche.turbo()