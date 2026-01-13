status = int(input("Ingrese el codigo de estatus:"))

match status:
    case 200:
        print("Codigo exitoso")
    case 404 | 403 | 407:
        print("El recurso no fue encontrado")
    case 500:
        print("Error en el servidor")
    case _:
        print("Codigo no existe")


