"""
Módulo 03: Estructuras Condicionales (if, elif, else).
Demuestra la clasificación de estados y lógica de decisiones con Type Hints.
"""


def clasificar_nivel_alerta_cpu(porcentaje_uso: float) -> str:
    """Clasifica el estado de uso de CPU según umbrales predefinidos."""
    if porcentaje_uso < 0.0 or porcentaje_uso > 100.0:
        return "ERROR: Valor fuera de rango válido (0-100)"
    elif porcentaje_uso < 50.0:
        return "NORMAL: Carga de trabajo estable"
    elif porcentaje_uso < 80.0:
        return "ADVERTENCIA: Carga elevandose"
    elif porcentaje_uso < 95.0:
        return "CRÍTICO: Alto consumo de recursos"
    else:
        return "EMERGENCIA: Servidor al límite de capacidad"


if __name__ == "__main__":
    mediciones = [35.2, 72.0, 88.5, 98.1, -5.0]

    print("=== Monitoreo de Recursos del Sistema ===")
    for medicion in mediciones:
        estado = clasificar_nivel_alerta_cpu(medicion)
        print(f"Uso: {medicion}% -> Estado: {estado}")