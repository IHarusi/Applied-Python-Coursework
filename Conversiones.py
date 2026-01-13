nomd_per = "Felipe"
aped_per = "Ruiz"
eda_per = 49
act_per = True
sue_per = 1200.555629
total_pro = "1900"

cadena = nomd_per + str(eda_per) #Para concatenar ambos debe tener el mismo tipo de dato

print(cadena)

prod_cadena = int(total_pro) * eda_per
print(prod_cadena)

sumas = int(sue_per) + eda_per
print(sumas)

#De manera ideal:

print(f"El nombre de la persona es {nomd_per} y si sueldo es {sue_per}")

# o con un número de decimales exactos
print(f"El nombre de la persona es {nomd_per} y si sueldo es {round(sue_per, 3)}")

#Para colocarlo como nueva variable
"""
Numero de digitos en total del número 
"""

nuevo_sueldo = f"{sue_per:.6}"
print(nuevo_sueldo)

#f de "formato"

"""
Numero de solo los decimales
"""
nuevo_sueldo2 = f"{sue_per:.2f}"
print(nuevo_sueldo2)
