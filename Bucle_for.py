
#Sintaxis del bucle for en Python

# Utilice el bucle for cuando conozca las veces que se repetirá el proceso. 

# for num in range(1, 11, 2): #Valor inicial, valor final, salto
#     print(f"{num}- ola")

# frutas = ["manzana", "banana", "cereza"]

# for fruta in frutas:
#     print(fruta)


cantidad_numeros = 0
suma_numeros = 0
for x in range(1, 6):
    numeros_ingresados = int(input("Ingrese un número:"))
    suma_numeros = suma_numeros + numeros_ingresados
    cantidad_numeros = cantidad_numeros + 1
print(f"La suma de los números ingresados es: {suma_numeros} y la cantidad de números ingresados es: {cantidad_numeros}")




    
