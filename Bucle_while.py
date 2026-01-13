#Se ejecuta un bloque de código mientras se cumpla una condición.
#Bloque de código. 

# contador = 0
# while contador < 5:
#     print(contador)
#     contador +=1


# suma = 0
# n = 1

# while suma < 20:
#     suma += n
#     n += 1
# print(f"la suma es {suma}")


usuario_valido = "Pepe125"
contraseña_valida = 12358
intentos = 3
persona = "Pepe pepon"

while intentos >0:
    usuario = input("Ingrese su nombre de usuario:")
    contraseña = input("Ingrese su contraseña:")
    if usuario == usuario_valido and contraseña == contraseña_valida:
        print(f"Acceso exitoso, sr {persona}")
        break
    else:
        intentos -= 1
        print(f"Usuario o contraseña incorrectos. Le quedan {intentos} intentos.")
if intentos == 0:
    print("El acceso ha sido bloqueado.")






