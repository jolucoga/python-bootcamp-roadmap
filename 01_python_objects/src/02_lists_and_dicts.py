"""
Módulo 01: Gestión de Colecciones (Listas y Diccionarios).
Demuestra el uso de listas, diccionarios y type hints en Python.
"""


def agregar_estudiante(
    registro: list[dict[str, str | float]],
    nombre: str,
    calificacion: float,
) -> list[dict[str, str | float]]:
    """Agrega un nuevo estudiante con su calificación al registro."""
    estudiante = {"nombre": nombre.title(), "calificacion": calificacion}
    registro.append(estudiante)
    return registro


def calcular_promedio(registro: list[dict[str, str | float]]) -> float:
    """Calcula el promedio general de las calificaciones en el registro."""
    if not registro:
        return 0.0

    suma_notas = sum(float(e["calificacion"]) for e in registro)
    return suma_notas / len(registro)


if __name__ == "__main__":
    lista_alumnos: list[dict[str, str | float]] = []

    agregar_estudiante(lista_alumnos, "ana garcía", 9.5)
    agregar_estudiante(lista_alumnos, "carlos lópez", 8.0)
    agregar_estudiante(lista_alumnos, "maría rodríguez", 9.0)

    promedio = calcular_promedio(lista_alumnos)

    print(f"Total de alumnos: {len(lista_alumnos)}")
    print(f"Promedio del grupo: {promedio:.2f}")