#importamos la clase mes
from class32mes import Mes
import random #libreria que introduce numeros enteros


#hago una tupla estática para automatizar los meses y ponerlos en un bucle
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
for nombreMes in meses:
    #print(nombreMes)
    mes = Mes()
    mes.nombre = nombreMes
    mes.temMax = random.randint(1,40) #introduce nº enteros entre el 1 y el 40
    mes.temMin = random.randint(1,40)

    x = mes.mediaMes()
    #print("La media de la temperatura de "+meses.nombre+ " es de: ",x, "ºC")
    print(x)
    print(mes)

