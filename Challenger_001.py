"""
Calcular el precio total de un producto IGV
"""
Precio_sin_igv = 100
IGV = 0.18
Precio_total = Precio_sin_igv + (Precio_sin_igv * IGV)
print(f"El precio total del producto con IGV es: {Precio_total:.2f}")

nombre_producto = input("Ingrese el nombre del producto:")
precio_producto = float(input("Ingrese el precio del producto:"))
cantidad_producto = int(input("Ingrese la cantidad del producto:"))
precio_total_producto = precio_producto * cantidad_producto
igv_a_pagar = precio_total_producto * 0.18
total_neto = precio_total_producto + igv_a_pagar
print(f"El producto es {nombre_producto} y su precio total es {total_neto:.2f}")


""""
2do ejercicio
"""

nombre_trabajador = input("Ingrese el nombre del trabajador:")
horas_trabajadas = int(input("Ingrese las horas trabajadas:"))
pago_por_hora = float(input("Ingrese el pago por hora:"))
salario_diario = horas_trabajadas * pago_por_hora
print(f"El trabajador {nombre_trabajador} tiene un salario diario de: {salario_diario:.2f}") 

"""
3er ejercicio
"""

nota_uno = float(input("Ingrese la primera nota:"))
nota_dos = float(input("Ingrese la segunda nota:"))
nota_tres = float(input("Ingrese la tercera nota:"))
promedio_notas = (nota_uno + nota_dos + nota_tres) / 3

if promedio_notas >= 11:
    print(f"El estudiante aprobó con un promedio de: {promedio_notas:.2f}")
else:
    print(f"El estudiante no aprobó con un promedio de: {promedio_notas:.2f}")

"""
4to ejercicio
"""

cantidad_dolares = float(input("Ingrese la cantidad en dólares:"))
tipo_de_cambio = float(input("Ingrese el tipo de cambio:"))
total_euros = cantidad_dolares * tipo_de_cambio
print(f"La cantidad en euros es: {total_euros:.2f} EUR")

"""
5to ejercicio
"""
total_segundos = int(input("Ingrese el total de segundos:"))
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos_restantes = total_segundos % 60
print(f"{horas} horas, {minutos} minutos, {segundos_restantes} segundos")


