
# Control de flujo: if, else, elif
try:
    Rapidez = float(input("Ingrese la rapidez del objeto:"))

    Posición = float(input("Ingrese la posición del objeto:"))

    if Rapidez > 0:
        if Posición > 0:
            print("El objeto se está moviendo en la dirección positiva.")
        else:
            print("El objeto se está moviendo en la dirección negativa.")

    if Rapidez == 0:
        if Posición == 0:
            print("El objeto está en reposo.")
        else:
            print("El objeto está en reposo pero no en el origen.")
    else:
        print("Condición no válida.")
except ValueError:
    print("Debe ingresar valores numéricos.")


nota_uno = float(input("Ingrese la primera nota: "))
nota_dos = float(input("Ingrese la segunda nota: "))
nota_tres = float(input("Ingrese la tercera nota: ")) 
promedio = (nota_uno + nota_dos + nota_tres) / 3

if promedio >= 11:
    print("Aprobado")
else:
    nota_sutitutoria = float(input("Ingrese la nota sustitutoria: "))
    nuevo_promedio = (nota_sutitutoria + promedio) / 2
    if nuevo_promedio >= 11:
        print("Aprobado en la sustitutoria")
    else:
        print("Reprobado")


"""
Ejemplo 2
"""
try:
    precio= float(input("Ingrese el precio del producto: "))

    if precio > 100:
        descuento = precio * 0.10
        precio_final = precio - descuento
        print(f"Se aplicó un descuento del 10%. El precio final es: {precio_final}")
    else:
        descuento = precio * 0.05
        precio_final = precio - descuento
        print(f"Se aplicó un descuento del 5%. El precio final es: {precio_final}")
except ValueError:
    print("Debe ingresar un valor numérico para el precio.")






