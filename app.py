#!/usr/bin/env python3
"""
Script simple que ejecuta un proceso básico.
Muestra información del sistema cada 5 segundos.
"""

import time
import datetime
import platform
import random


def proceso_simple():
    """Función que ejecuta un proceso simple de manera continua"""
    contador = 0
    print("=" * 12)
    print("🚀 Aplicación Python iniciada")
    print(f"Sistema operativo: {platform.system()}")
    print(f"Versión de Python: {platform.python_version()}")
    print("=" * 12)

    try:
        while True:
            contador += 1
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            numero_aleatorio = random.randint(1, 100)

            print(
                f"[{timestamp}] Iteración #{contador} - Número generado: {numero_aleatorio}"
            )

            # Simular un proceso simple
            if numero_aleatorio > 80:
                print(f"  ✓ Número alto detectado: {numero_aleatorio}")
            elif numero_aleatorio < 20:
                print(f"  ⚠ Número bajo detectado: {numero_aleatorio}")

            # Esperar 5 segundos antes de la siguiente iteración
            time.sleep(5)

    except KeyboardInterrupt:
        print("\n" + "=" * 12)
        print(f"🛑 Aplicación detenida después de {contador} iteraciones")
        print("=" * 12)


if __name__ == "__main__":
    proceso_simple()
