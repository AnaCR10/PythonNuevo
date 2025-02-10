print("Por favor introduce las horas extras trabajadas")
horas_trabajadas =int(input())
horas_extra = horas_trabajadas - 36
print("Ahora los kilómetros")
km = int(input())
print("Cuál es el precio hora?")
precio_hora = int(input())
dietas = ""
if (km < 100):
    dietas = "locales"
elif (101 < km < 500):
    dietas = "provinciales"
else:
    dietas = "nacionales"
print("Dietas ", dietas)

salario_total = 0
salario_extra = 0
salario_base = 36 * precio_hora

if (horas_trabajadas > 36):
    salario_extra = (precio_hora +2 )* horas_extra
  
else:
    #no ha hecho horas extra
    horas_extra = 0
    salario_extra = 0
    salario_base = horas_trabajadas * precio_hora

salario_total= salario_base + salario_extra

if (salario_total < 250):
    retencion = "0"
elif (251 < salario_total < 600):
    retencion = "20"
else:
    retencion = "40"

print("Retencion es, ", retencion)
print("Salario total, ", salario_total)
print("Salario base, ", salario_base)
print("Salario extra, ", salario_extra)
#solución profe, la mía parece estar bien pero el enunciado no es muy claro
# print("Ejemplo Horas extra")
# print("Horas trabajadas")
# horasTrabajadas = int(input())
# print("Precio hora")
# precioHora = int(input())
# print("Kilometros recorridos")
# km = int(input())
# horasExtra = 0
# salarioExtra = 0
# salarioBase = 0
# salarioTotal = 0
# dietas = ""
# retencion = ""
# #PREGUNTAMOS SI TENEMOS HORAS EXTRA
# if (horasTrabajadas > 36):
#     #HORAS EXTRA
#     horasExtra = horasTrabajadas - 36
#     salarioBase = precioHora * 36
#     salarioExtra = horasExtra * (precioHora + 2)
# else:
#     #NO HA HECHO HORAS EXTRA
#     horasExtra = 0
#     salarioExtra = 0
#     salarioBase = horasTrabajadas * precioHora
# salarioTotal = salarioBase + salarioExtra
# if (km <= 100):
#     dietas = "LOCALES"
# elif (km >= 101 and km <= 500):
#     dietas = "PROVINCIALES"
# else:
#     dietas= "NACIONALES"
# if (salarioTotal < 250):
#     retencion = "SIN RETENCION"
# elif (salarioTotal >= 250 and salarioTotal <= 600):
#     retencion = "20% Retencion"
# else:
#     retencion = "40% Retención"
# #INFORME
# print("Informe de salario")
# print("Horas trabajadas ", horasTrabajadas)
# print("Horas extra ", horasExtra)
# print("Precio hora ", precioHora)
# print("Precio extra ", (precioHora + 2))
# print("Salario base ", salarioBase)
# print("Salario extra ", salarioExtra)
# print("Salario total ", salarioTotal)
# print("Retenciones ", retencion)
# print("Dietas ", dietas)



