"""
Módulo 03: Bucles WHILE y Sentencias de Control.
Demuestra la gestión de intentos, reintentos de conexión y uso de break/continue.
"""


def simular_reintento_conexion(max_intentos: int = 3) -> bool:
    """Simula intentos de reconexión a un servicio hasta lograr éxito o agotar intentos."""
    intento = 1
    conexion_exitosa = False

    while intento <= max_intentos:
        print(f"Intento {intento} de {max_intentos} conectando al servicio...")
        
        # Simulación: éxito en el tercer intento
        if intento == 3:
            conexion_exitosa = True
            print(" Conexión establecida con éxito.")
            break  # Sale del bucle antes de agotar la condición

        intento += 1

    return conexion_exitosa


if __name__ == "__main__":
    print("=== Cliente de Servicio de Red ===")
    exito = simular_reintento_conexion()
    print(f"Resultado final: {'Operativo' if exito else 'Fallo de Red'}")