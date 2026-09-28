"""
Módulo 02: Operadores Lógicos Encadenados.
Demuestra la combinación de condiciones complejas usando and, or, not
y sintaxis encadenada de Python (a < b < c).
"""


def verificar_acceso_sistema(
    usuario_activo: bool,
    nivel_rol: int,
    intentos_fallidos: int,
    es_mantenimiento: bool,
) -> bool:
    """
    Determina si un usuario puede ingresar al sistema basado en reglas de negocio:
    - Debe estar activo y no estar el sistema en mantenimiento.
    - O bien, debe tener rol de Administrador (nivel >= 5) sin importar mantenimiento.
    - No debe haber superado el límite de 3 intentos fallidos.
    """
    sin_bloqueo_seguridad = intentos_fallidos < 3
    es_admin = nivel_rol >= 5

    # Evaluación lógica combinada
    acceso_permitido = sin_bloqueo_seguridad and (
        (usuario_activo and not es_mantenimiento) or es_admin
    )

    return acceso_permitido


if __name__ == "__main__":
    print("=== Validador de Reglas de Acceso ===")

    # Caso 1: Usuario estándar intentando entrar durante mantenimiento
    acceso_1 = verificar_acceso_sistema(
        usuario_activo=True,
        nivel_rol=1,
        intentos_fallidos=0,
        es_mantenimiento=True,
    )
    print(f"Usuario Estándar en Mantenimiento -> Acceso: {acceso_1}")

    # Caso 2: Admin entrando durante mantenimiento
    acceso_2 = verificar_acceso_sistema(
        usuario_activo=True,
        nivel_rol=5,
        intentos_fallidos=1,
        es_mantenimiento=True,
    )
    print(f"Admin en Mantenimiento -> Acceso: {acceso_2}")

    # Demostración de comparaciones encadenadas propias de Python:
    # En Python se puede escribir 0 <= x <= 100 en lugar de (x >= 0 and x <= 100)
    porcentaje_uso_ram = 85.0
    uso_normal = 0 <= porcentaje_uso_ram <= 90
    print(f"\nUso de RAM ({porcentaje_uso_ram}%) en rango normal: {uso_normal}")