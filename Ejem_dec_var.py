"""
Ejemplos varios de declaracion de variables

"""

#Asignacion simple

nomb = "Pedro"
aped = "Torre"
cantid = 20

#Asignacion multiple

cant_pr, mensj_bien, estado = 5, "Hola", True

print(cant_pr)

#Asignar el mismo valor

t = i = o = 20

print(t)

#Variables especiales (estructura de datos)
"""

LIST
DICCIONARIOS
DUPLAS
CONJUNTOS

"""

Cursos = ["Python", "Django", "Flask", 20, 140.2, ["Fastapi", "Pandas"]] #List

print(type(Cursos)) 

#List es mutable (Se puede modificar el contenido)

Empleados = {"Codigo" : "200", "Nombre" : "Armando", "Apellido" : "De la Cruz"} #Dict (Clave - Valor)

print(Empleados["Apellido"])

#Dict tmb es mutable

Valores = (100, 200, 400) #Tupla

#Tupla es inmutable

Datos1 = {200, 4500, 4050, 3, 5, 8} #set

#Set es mutable

print(Datos1)



#Ver palabras restringidas de python

import keyword
print(keyword.kwlist)

print(keyword.iskeyword(Datos1))