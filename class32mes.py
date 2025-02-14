class Mes:
    nombre=""
    temMax = 0
    temMin = 0
    def __str__(self):
        return self.nombre +",Temperatura Máxima "+ str(self.temMax)+", Temperatura Mínima "+str(self.temMin)
    def getTemMaxima(self):
        print("La temperatura Máxima es de: ")
        return self.temMax
    def getTemMinima(self):
        print("La temperatura Mínima es de: ")
        return self.temMin
    def mediaMes(self):
        media = (self.temMax + self.temMin) / 2
        return media
    
    
