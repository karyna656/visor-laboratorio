import re

# Esto es lo que el sistema busca para bloquear
reglas = ["OR '1'='1'", "DROP TABLE", "script"]

def revisar_entrada(texto):
    print(f"Analizando: {texto}")
    for regla in reglas:
        if regla in texto:
            print("❌ ¡ATAQUE DETECTADO! Bloqueando acceso...")
            return
    print("✅ Todo legal. Acceso permitido.")

# Probamos el sistema
revisar_entrada("Informe médico: El paciente está bien.")
revisar_entrada("Admin' OR '1'='1'") # Esto es un intento de hackeo
