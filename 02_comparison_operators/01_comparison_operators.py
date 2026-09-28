"""
Módulo 02: Operadores de Comparación.
Demuestra la evaluación de igualdad, desigualdad y rangos numéricos.
"""


def validar_temperatura_servidor(
    temp_actual: float, temp_max_permitida: float
) -> dict[str, bool]:
    """Evalúa la temperatura de un servidor contra los límites operativos."""
    es_temperatura_optima = temp_actual < temp_max_permitida
    es_alerta_critica = temp_actual >= temp_max_permitida
    es_exactamente_limite = temp_actual == temp_max_permitida

    return {
        "optimo": es_temperatura_optima,
        "critico": es_alerta_critica,
        "en_limite": es_exactamente_limite,
    }


if __name__ == "__main__":
    limite_cpu = 75.0
    lecturas_temp = [68.5, 75.0, 82.3]

    print("=== Control de Temperatura de Hardware ===")
    for temp in lecturas_temp:
        estado = validar_temperatura_servidor(temp, limite_cpu)
        print(
            f"Temp: {temp}°C | Óptimo: {estado['optimo']} | "
            f"Crítico: {estado['critico']} | En límite: {estado['en_limite']}"
        )