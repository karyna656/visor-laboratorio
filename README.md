# 🏥 Visor Seguro de Resultados de Laboratorio

Aplicación web de Python + Flask para visualización segura de resultados de laboratorio médico, implementando principios de seguridad SC-900.

## 🛡️ Características de Seguridad

- **Autenticación Multifactor (MFA)**: Validación con contraseña + código por email
- **Control de Acceso Basado en Roles**: Pacientes solo ven sus resultados
- **Confianza Cero**: Cada solicitud se verifica explícitamente
- **Cifrado de Datos**: Contraseñas con hash seguro (werkzeug.security)
- **Sesiones Seguras**: Expiración automática tras 15 minutos de inactividad

## 🚀 Instalación

### 1. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Inicializar base de datos
```bash
python app.py
```

### 4. Ejecutar la app
```bash
python app.py
```

La app estará disponible en: `http://localhost:5000`

## 📋 Estructura del Proyecto

```
visor-laboratorio/
├── app.py              # Archivo principal (Flask)
├── requirements.txt    # Dependencias Python
├── .gitignore         # Archivos ignorados
├── static/            # CSS, JS, imágenes
│   ├── css/
│   └── js/
├── templates/         # Plantillas HTML
│   ├── login.html
│   ├── dashboard.html
│   └── resultados.html
└── README.md         # Este archivo
```

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
