def sumaNumero(a,b):
    resultado = a+b
    return resultado

def restaNumeros(a,b):
    resultado = a-b
    return resultado

def multiplicaNumeros(a,b):
    resultado = a*b
    return resultado

def mostrarMenu ():
    print("Seleccione una opción")
    print("1.- Suma los números")
    print("2.- Resta")
    print("3.- Multiplica")
    print("4.- Salir")

print("OPERACIONES MATEMÁTICAS")
print("Introduzca el número 1")
num1 = int(input())
print("Introduzca el número 2")
num2 = int(input())

mostrarMenu()
resultado= ""
opcion = int(input())
while (opcion!= 4):
    
    if(opcion == 1):
        resultado = sumaNumero(num1,num2)
    elif (opcion == 2):
        resultado = restaNumeros(num1,num2)
    elif (opcion == 3):
        resultado = multiplicaNumeros(num1,num2)
    else:
        mostrarMenu()
print ("El resultado es, " + resultado)
print ("Fin del programa")
