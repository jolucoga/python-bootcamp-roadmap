"""
Módulo 03: Bucles FOR y Desempaquetado de Datos.
Demuestra iteraciones sobre estructuras compuestas y uso de range/enumerate.
"""


def procesar_transacciones(
    transacciones: list[tuple[str, float]]
) -> dict[str, float]:
    """Suma los ingresos y egresos a partir de una lista de transacciones."""
    totales = {"ingresos": 0.0, "egresos": 0.0}

    # Desempaquetado directo de la tupla (tipo, monto)
    for tipo, monto in transacciones:
        if tipo.lower() == "ingreso":
            totales["ingresos"] += monto
        elif tipo.lower() == "egreso":
            totales["egresos"] += monto

    return totales


if __name__ == "__main__":
    historial: list[tuple[str, float]] = [
        ("ingreso", 1500.00),
        ("egreso", 230.50),
        ("ingreso", 800.00),
        ("egreso", 120.00),
    ]

    resumen = procesar_transacciones(historial)
    balance = resumen["ingresos"] - resumen["egresos"]

    print("=== Balance Financiero ===")
    print(f"Total Ingresos: ${resumen['ingresos']:.2f}")
    print(f"Total Egresos:  ${resumen['egresos']:.2f}")
    print(f"Balance Net:    ${balance:.2f}")