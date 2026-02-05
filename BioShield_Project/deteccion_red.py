# Simulación de detección de escaneo (comportamiento anómalo)
intentos_conexion = 0
limite_seguro = 5

def monitorear_red(ip_origen):
    global intentos_conexion
    intentos_conexion += 1
    
    if intentos_conexion > limite_seguro:
        print(f"🚨 ALERTA: La IP {ip_origen} está haciendo ESCANEO DE RED.")
        return "BLOQUEAR"
    return "PERMITIR"

# Pruebas del sistema
print("Probando el sistema de monitoreo de red:")
for i in range(7):
    ip = f"192.168.1.{i+1}"
    resultado = monitorear_red(ip)
    print(f"Conexión desde {ip}: {resultado}")
    