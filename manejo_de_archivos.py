"""
'r' : Modo de lectura (por defecto). El archivo debe existir.
'w' : Modo de escritura. Crea un archivo nuevo o trunca el archivo existente.
'a' : Modo de anexado. Crea un archivo nuevo o agrega datos al final del archivo existente.
'b' : Modo binario. Se puede combinar con los otros modos (por ejemplo, 'rb' para leer en 
'x' : Modo exclusivo. Crea un nuevo archivo, pero fallará si el archivo ya existe.
"""

with open('Nivel_Básico/probando.txt','r',encoding='utf-8') as file:
    contenido=file.read()
    print(contenido)


#with open('Nueva_Informacion.txt','w',encoding='utf-8') as file:
#    file.write("Primera Linea de Texto.\n")
#    file.write("Segunda Linea de Texto.\n")

with open("Nueva_informacion.txt", "w", encoding = "utf-8") as file:
    file.write("Primera linea de texto.\n")
    file.write("Segunda linea de texto.\n")

with open("Nueva_informacion.txt", "w", encoding = "utf-8") as file:
    file.write("Primera linea de texto.\n")
    file.write("Segunda linea de texto.\n")


