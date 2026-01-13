"""
Ambito local
"""

def mi_funcion():
    variable_local = 30
    print(variable_local)

#mi_funcion()

"""
Ambito Global
"""

COUNT = 1

def mi_funcion_2():
    global COUNT
    COUNT +=1
    print(COUNT)

#mi_funcion_2()

def mi_funcion_3(COUNT):
    COUNT +=1
    print(COUNT)

mi_funcion_3(COUNT)

a = 4
b = 5

def suma_var(a, b):
    print(a + b)

suma_var(a,b)

def funcion_4():
    z = 30
    print(z ** 2)

funcion_4()

