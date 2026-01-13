from Ejercicios_varios import calcular_cambio



def test_cambio_con_decimales():
    # Caso 2: Costo 1.50, Pagado 2.00 (debe dar una moneda de 0.5)
    resultado = calcular_cambio(2.00, 1.50)
    assert resultado == {0.5: 1}

