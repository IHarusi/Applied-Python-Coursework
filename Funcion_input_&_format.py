"""
Funcion input
"""
"""
Nombre_producto = input("Ingrese el nombre del producto:")
Precio_producto = int(input("Ingrese precio del producto:"))
Cantidad_producto = int(input("Ingrese la cantidad del producto:"))
#print(f"El producto es {Nombre_producto} y su precio total es {Precio_producto * Cantidad_producto}")
"""
"""
Funcion format
"""

#"Cadena de texto {}".format(valor)

e = 2.14152222222222222222222545148454815415454545764276216721721217217621762176127612716726721762176121

Valor_reducido_e = "EL valor reducido de e es {:.20f}".format(e)

#print(Valor_reducido_e)


#Ejercicio

Vo = int(input("Ingrese la rapidez inicial:"))
Xo = int(input("Ingrese posición inicial:"))
if Vo >= 0 and Xo >= 0:
    print("Valores iniciales estables")
elif Xo < 0 or Vo < 0:
    print("Posición y/o rapidez no válida")




