# #Break se usa para salir inmediatamente de un bucle. 

# for i in range(10):
#     if i == 4:
#         break
#     print(i)

# contador = 0
# while contador < 10:
#     if contador == 0:
#         break
#     print(contador)
#     contador += 1

# while True:
#     if contador >= 4:
#         break
#     print(contador)
#     contador += 1

# #Continue se usa para saltar a la siguiente iteración del bucle.

# for i in range(10):
#     if i % 2 == 0:
#         continue  #Saltar cuando el numero sea par
#     print(i)

# contador = 0
# while contador < 10:
#     if contador % 2 == 0:
#         continue  #Saltar cuando el numero sea par
#     print(contador)
#     contador += 1

# #Else se ejecuta si el bucle no fue interrumpido por un break.

# frutas = ["manzana", "banana", "cereza"]
# for fruta in frutas:
#     print(frutas)
# else:
#     print("Se han listado todas las frutas.")

contador = 0
while contador < 5:
    print(contador)
    contador +=1
else:
    print("El bucle ha terminado sin interrupciones.")

