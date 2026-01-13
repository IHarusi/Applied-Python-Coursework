"""
Calcular el cambio de una transacción
"""

def calcular_cambio(Costo, pagado):
    if pagado < Costo:
        return "Dinero insuficiente, intente de nuevo"
    if pagado == Costo:
        return "Pago exacto, no hay cambio."
    cambio = pagado - Costo
    billetes_monedas = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    desglose = {}
    for valor in billetes_monedas:
        cantidad = int(cambio // valor)
        cambio = round(cambio % valor, 2)
        if cantidad > 0:
            desglose[valor] = cantidad
    return desglose

Costo = 20
pagado = 10
print(calcular_cambio(20, 20))

{}