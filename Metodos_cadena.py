nombre_curso = "python"

Nueva_Cadena = nombre_curso.upper() #Todo en mayúscula
Nueva_Cadena_2 = Nueva_Cadena.lower() #Todo en min+isucla

Mensaje = " Hola mundo "
Mensaje_sin = Mensaje.strip()

#print(Mensaje_sin)

Mensaje_de_bien = "Hola mundo desde python"
cadena_buscar = Mensaje_de_bien.find("python") #Si no lo encuentra da -1
cadena_buscar = Mensaje_de_bien.index("python") # Si no lo encuentra da valuerror

print(cadena_buscar)

Mensaje_de_bien = "Hola mundo desde python"
cadena_reemplazo = Mensaje_de_bien.replace("python", "Django") #Reemplazar con una subcadena la cadena principal

palabras = ["Manzana", "Banana", "Cereza"]
resultado = ", ".join(palabras)

print(resultado)
print(palabras)

