"""
Módulo 01: Tuplas, Conjuntos (Sets) y Booleanos.
Demuestra la inmutabilidad de tuplas, eliminación de duplicados con sets
y evaluaciones de verdad con booleanos.
"""


def procesar_log_accesos(
    entradas: list[tuple[str, str, bool]]
) -> dict[str, set[str] | int]:
    """
    Procesa una lista de accesos (tuplas) y retorna un resumen con:
    - Usuarios únicos que iniciaron sesión exitosamente (Set).
    - Cantidad total de intentos fallidos (Int).
    """
    usuarios_exitosos: set[str] = set()
    intentos_fallidos: int = 0

    for ip, usuario, exito in entradas:
        # Evaluamos la condición booleana
        if exito:
            usuarios_exitosos.add(usuario)
        else:
            intentos_fallidos += 1

    return {
        "usuarios_unicos": usuarios_exitosos,
        "fallos_totales": intentos_fallidos,
    }


if __name__ == "__main__":
    # Datos de prueba usando Tuplas: (IP, Usuario, Éxito)
    logs_servidor: list[tuple[str, str, bool]] = [
        ("192.168.1.10", "admin", True),
        ("192.168.1.11", "dev_user", True),
        ("192.168.1.12", "admin", True),  # Duplicado exitoso
        ("192.168.1.13", "invitado", False),
        ("192.168.1.14", "hacker_user", False),
    ]

    resumen = procesar_log_accesos(logs_servidor)

    print("=== Resumen de Accesos al Servidor ===")
    print(f"Usuarios únicos autenticados: {resumen['usuarios_unicos']}")
    print(f"Intentos fallidos de acceso: {resumen['fallos_totales']}")

    # Demostración breve de inmutabilidad en tuplas
    coordenada_servidor: tuple[float, float] = (20.6597, -103.3496)
    print(f"\nUbicación del servidor (Lat, Lon): {coordenada_servidor}")