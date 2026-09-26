"""
Módulo 01: Conceptos Básicos de Números y Cadenas en Python.
Demuestra operaciones elementales, formateo de texto y Type Hints.
"""

def calcular_descuento(precio_original: float, porcentaje_descuento: float) -> float:
    """Calcula el precio final aplicando un porcentaje de descuento."""
    descuento = precio_original * (porcentaje_descuento / 100)
    return precio_original - descuento


def formatear_resumen_producto(nombre: str, precio: float, descuento: float) -> str:
    """Retorna una cadena formateada con el resumen de la compra usando f-strings."""
    precio_final = calcular_descuento(precio, descuento)
    return (
        f"Producto: {nombre.title()}\n"
        f"Precio Original: ${precio:.2f}\n"
        f"Descuento: {descuento}%\n"
        f"Precio Final: ${precio_final:.2f}"
    )


if __name__ == "__main__":
    # Prueba manual de las funciones
    producto = "laptop gamer"
    precio_base = 1250.00
    descuento_aplicado = 15.0

    resumen = formatear_resumen_producto(
        producto, precio_base, descuento_aplicado
    )
    print(resumen)