"""
Sistema de registro de ventas
-Guardas cada venta (con detalles de producto, cantidad y precio) en un archivo de texto
-Mostrar un reporte
-Cada vez que se realize una venta registralo en el archivo "Ventas.txt."

"""
def registrar_venta(producto, cantidad, precio_unitario):
    with open("Ventas.txt", "a") as archivo:
        total = cantidad * precio_unitario
        archivo.write(f"Producto: {producto}, Cantidad: {cantidad}, Precio Unitario: {precio_unitario}, Total: {total}\n")
    print(f"Venta registrada: {producto}, Cantidad: {cantidad}, Precio Unitario: {precio_unitario}, Total: {total}")

