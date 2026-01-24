# 🏥 Visor Seguro de Resultados de Laboratorio

Aplicación web de Python + Flask para visualización segura de resultados de laboratorio médico, implementando principios de seguridad SC-900.

## 🛡️ Características de Seguridad

- **Autenticación Multifactor (MFA)**: Validación con contraseña + código por email
- **Control de Acceso Basado en Roles**: Pacientes solo ven sus resultados
- **Confianza Cero**: Cada solicitud se verifica explícitamente
- **Cifrado de Datos**: Contraseñas con hash seguro (werkzeug.security)
- **Sesiones Seguras**: Expiración automática tras 15 minutos de inactividad

## 🚀 Instalación y Prueba

### 1. Clonar el repositorio
```bash
git clone https://github.com/karyna656/visor-laboratorio.git
cd visor-laboratorio
```

### 2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

---

## 🔐 Credenciales de Prueba

```
DNI:         12345678
Contraseña:  demo123
Nombre:      Sandra Carina Paijes
```

### Pasos para probar:
1. Abre http://localhost:5000 en tu navegador
2. Inicia sesión con las credenciales de arriba
3. Verás el dashboard con un resultado de laboratorio
4. Haz clic en el resultado para ver más detalles
5. Intenta acceder a `/resultado/999` - verás error 403 (seguridad)

---

## 📋 Características Implementadas

✅ **Autenticación Segura**
- Login/Registro de pacientes
- Contraseñas hasheadas con werkzeug.security
- Validación de credenciales

✅ **Dashboard Personal**
- Cada paciente ve solo sus resultados
- Estado del resultado (Pendiente, Listo, Revisado)
- Interfaz amigable y responsiva

✅ **Seguridad**
- Control de acceso: Error 403 si intentas ver resultado de otro paciente
- Sesiones con validación
- Base de datos SQLite local

✅ **Funcionalidades**
- Ver resultados de laboratorio
- Detalles de cada estudio
- Descarga de PDF (en desarrollo)

---

## 🔐 Casos de Prueba (SC-900)

| Test ID | Descripción | Resultado Esperado |
|---------|------------|-------------------|
| T01 | Login con credenciales inválidas | Rechazo + Mensaje de error |
| T02 | Intento de acceder a resultado de otro paciente | Error 403 Prohibido |
| T03 | Sesión expira tras 15 min inactividad | Redirección a login |

## 👨‍💻 Ejemplo de Uso

1. **Registrarse** como paciente (DNI + Contraseña)
2. **Ingresar credenciales** para autenticación
3. **Ver resultados personales** (cifrados en BD)
4. **Descargar PDF** con privacidad garantizada

## ⚙️ Tecnologías

- **Backend**: Flask (Python web framework)
- **Base de Datos**: SQLAlchemy + SQLite (producción: PostgreSQL)
- **Seguridad**: werkzeug.security (hashing de contraseñas)
- **Frontend**: HTML5, CSS3, Bootstrap
