from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os

# Inicializar Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu-clave-secreta-cambiar-en-produccion'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laboratorio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos
db = SQLAlchemy(app)

# ===== MODELOS DE BASE DE DATOS =====

class Paciente(db.Model):
    """Modelo de Paciente"""
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(11), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    resultados = db.relationship('Resultado', backref='paciente', lazy=True)
    
    def __repr__(self):
        return f'<Paciente {self.nombre}>'

class Resultado(db.Model):
    """Modelo de Resultado de Laboratorio"""
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    tipo_estudio = db.Column(db.String(100), nullable=False)  # Ej: "Análisis de Sangre"
    fecha_estudio = db.Column(db.DateTime, nullable=False)
    resultado = db.Column(db.Text, nullable=False)  # Datos del resultado (CSV o JSON)
    estado = db.Column(db.String(20), default='Pendiente')  # Pendiente, Listo, Revisado
    fecha_creacion = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return f'<Resultado {self.tipo_estudio} - {self.estado}>'

# ===== RUTAS =====

@app.route('/')
def index():
    """Página de inicio"""
    if 'paciente_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login de paciente"""
    if request.method == 'POST':
        dni = request.form.get('dni')
        password = request.form.get('contraseña')

        # Buscar paciente en BD
        paciente = Paciente.query.filter_by(dni=dni).first()

        if paciente and check_password_hash(paciente.password, password):
            # Contraseña correcta
            session['paciente_id'] = paciente.id
            session['nombre'] = paciente.nombre
            return redirect(url_for('dashboard'))
        else:
            # Credenciales inválidas
            return render_template('login.html', error='DNI o contraseña incorrectos')
    
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """Registro de nuevo paciente"""
    if request.method == 'POST':
        dni = request.form.get('dni')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('contraseña')
        
        # Verificar si DNI ya existe
        if Paciente.query.filter_by(dni=dni).first():
            return render_template('registro.html', error='El DNI ya está registrado')
        
        # Crear nuevo paciente
        paciente = Paciente(
            dni=dni,
            nombre=nombre,
            email=email,
            password=generate_password_hash(password)
        )
        
        try:
            db.session.add(paciente)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            return render_template('registro.html', error='Error al registrar. Intenta de nuevo.')
    
    return render_template('registro.html')

@app.route('/dashboard')
def dashboard():
    """Panel de control del paciente"""
    # Verificar sesión activa
    if 'paciente_id' not in session:
        return redirect(url_for('login'))
    
    paciente = Paciente.query.get(session['paciente_id'])
    resultados = Resultado.query.filter_by(paciente_id=paciente.id).all()
    
    return render_template('dashboard.html', paciente=paciente, resultados=resultados)

@app.route('/resultado/<int:resultado_id>')
def ver_resultado(resultado_id):
    """Ver detalle de un resultado (Control de Acceso)"""
    if 'paciente_id' not in session:
        return redirect(url_for('login'))
    
    resultado = Resultado.query.get(resultado_id)
    
    # SEGURIDAD: Verificar que el resultado pertenece al paciente logueado
    if resultado.paciente_id != session['paciente_id']:
        return "Error 403: Prohibido", 403
    
    return render_template('resultado.html', resultado=resultado)

@app.route('/logout')
def logout():
    """Cerrar sesión"""
    session.clear()
    return redirect(url_for('login'))

# ===== INICIALIZAR BD =====

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Crear datos de ejemplo (solo en desarrollo)
        if Paciente.query.count() == 0:
            paciente_demo = Paciente(
                dni='12345678',
                nombre='Sandra Carina Paijes',
                email='sandra@example.com',
                password=generate_password_hash('demo123')
            )
            db.session.add(paciente_demo)
            db.session.commit()
            
            # Resultado de ejemplo
            resultado_demo = Resultado(
                paciente_id=paciente_demo.id,
                tipo_estudio='Análisis de Sangre',
                fecha_estudio=datetime.now(),
                resultado='Glucosa: 100 mg/dL | Colesterol: 180 mg/dL',
                estado='Listo'
            )
            db.session.add(resultado_demo)
            db.session.commit()
    
    # Ejecutar app
    app.run(debug=True, port=5000)
