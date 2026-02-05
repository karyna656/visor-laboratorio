# 🧪 Plan de Pruebas: Monitor de Seguridad SOC - MediGuard

Este documento detalla el protocolo de pruebas realizado para el Simulador de Alertas Críticas, asegurando que la respuesta ante incidentes cumpla con los estándares de disponibilidad y visibilidad.

---

## 🛡️ Casos de Prueba de Ciberseguridad (SOC)

| ID | Escenario de Prueba | Resultado Esperado | Prioridad |
|:---|:---|:---|:---|
| SOC-01 | **Detección Automática** | Tras 5 segundos de inactividad, el sistema debe disparar la alerta de intruso sin intervención humana. | Crítica |
| SOC-02 | **Protocolo de Sirena** | Al activarse la alerta, debe emitirse un sonido de sirena (oscilador) para notificar al administrador. | Alta |
| SOC-03 | **Bloqueo de Amenaza** | Al presionar "BLOQUEAR AMENAZA", el sistema debe detener la sirena y reiniciar el monitoreo limpio. | Crítica |

---

## 📱 Pruebas de Experiencia de Usuario (Mobile QA)

| ID | Atributo | Verificación Realizada | Estado |
|:---|:---|:---|:---|
| MOB-01 | **Visibilidad P1** | En dispositivos móviles, el texto "INTRUSO" debe ocupar el 80% de la pantalla para evitar distracciones. | Pasado ✅ |
| MOB-02 | **Vibración Háptica** | El dispositivo debe vibrar al detectarse la amenaza (en navegadores compatibles). | Pasado ✅ |
| MOB-03 | **Contraste de Alerta** | El parpadeo Rojo/Negro debe ser lo suficientemente intenso para ser visto a distancia. | Pasado ✅ |

---

## ⚙️ Conceptos de Azure SC-900 Validados

* **SIEM (Microsoft Sentinel):** La lógica de logs simula la recolección de eventos de seguridad.
* **SOAR:** El botón de bloqueo representa la automatización de la respuesta para reducir el tiempo de exposición (MTTR).
* **Defensa en Profundidad:** Se aplican múltiples canales de alerta (Visual, Auditivo y Táctil).

---
**Nota de QA:** Se recomienda al usuario interactuar con la pantalla (un clic inicial) para otorgar permisos de audio al navegador.