print("Introduce el primer número")
num1 = int(input())
print("Introduce el segundo número")
num2 = int(input())
print("Introduce el tercer número")
num3 = int(input())
# creamos tres variables para ir guardando las respuestas según vayamos haciendo preguntas, y las inicializamos a cero
mayor = 0
menor = 0
intermedio = 0
#comparamos cada número con los otros dos
# primero buscamos el mayor
if (num1 >= num2 and num1 >= num3):
    mayor = num1
elif (num2 >=1 and num2 >= num2):
    mayor = num2
else:
    mayor = num3 
# ahora buscamos el menor   
if (num1 <= num2 and num1 <= num3):
    menor = num1
elif (num2 <=1 and num2 <= num2):
    menor = num2
else:
    menor = num3
#el intermedio es por descarte 
suma = num1 + num2 + num3
intermedio = suma - mayor - menor
print ("Mayor ", mayor)
print("Menor ", menor)
print("Intermedio ", intermedio)
