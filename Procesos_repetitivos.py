"""
Buscamos un numero en una lista y al encontrarlo usar breake para salir del bucle
"""

numeros = [1, 3, 5, 7, 9, 11, 13, 15]
objetivo = int(input("Ingrese el número a buscar: "))

for numero in numeros:
    if numero == objetivo:
        print(f"Número {objetivo} encontrado")
        break
else: 
    print("Número no encontrado")


"""
Imprime los numeros de una lista, pero salta los numeros pares
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for numero in numeros:
    if numero % 2 == 0:
        continue # Saltar los números pares
    print(numero)


"""
While
"""
#Hasta que ingrese el número "0". Salir del programa

while True:
    numero = int(input("Ingrese un numero para salir (0 para salir)"))
    if numero == 0:
        print("Saliendo del bucle...")
        break


#Solicitar numeros al usuario pero si el numero es negativo lo voy a ignorar. Solo se imprimirá los numeros positivos. 

while True:
    numero = int(input("Introduce un numero positivo:"))
    if numero < 0:
        print("Numero negativo IGNORADO")
        continue
    if numero == 0:
        print("Saliento del bucle")
        break

