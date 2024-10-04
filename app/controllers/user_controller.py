#vamos a definir la lógica para el registro, login y perfil, utilizando consultas SQL manuales. Este código se conecta directamente a la base de datos y ejecuta consultas SQL para el login, registro, y el perfil de usuario.
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_bcrypt import Bcrypt
from flask import session
import os
from werkzeug.utils import secure_filename


user_bp = Blueprint('user_bp', __name__)
bcrypt = Bcrypt()

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    connection = current_app.connection
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        email = request.form['email']
        password = request.form['password']
        documento = request.form['documento']
        telefono = request.form['telefono']
        segundo_telefono = request.form['segundo_telefono']
        direccion = request.form['direccion']
        cargo = request.form['cargo']

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO usuarios (nombres, apellidos, email, password, documento, telefono, segundo_telefono, direccion, cargo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (nombres, apellidos, email, password, documento, telefono, segundo_telefono, direccion, cargo)
                )
                connection.commit()
            return redirect(url_for('user_bp.Inicio'))
        except Exception as e:
            return str(e)

    # Obtener roles para el formulario de registro
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, nombre_cargo FROM cargo")  # Asegúrate de que esta columna exista en la tabla cargo
            cargos = cursor.fetchall()
    except Exception as e:
        return str(e)

    return render_template('Inicio.html', cargos=cargos)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = current_app.connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, password, cargo_id FROM usuarios WHERE email=%s", (email,))
                result = cursor.fetchone()
                if result and bcrypt.check_password_hash(result['password'], password):
                    session['user_id'] = result['id']  # Guardar el ID del usuario en la sesión
                    session['user_cargo'] = result['cargo_id']  # Guardar el rol del usuario en la sesión
                    return redirect(url_for('user_bp.dashboard'))  # Redirigir al dashboard
                else:
                    return "Login Failed"
        except Exception as e:
            return str(e)

    return render_template('Inicio_Sesión.html')


@user_bp.route('/dashboard')
def dashboard():
    # Redirigir al usuario a su página según el cargo
    cargo_id = session.get('user_cargo')

    if cargo_id == 1:  # Gerente
        return redirect(url_for('user_bp.Gerente_1.html'))
    elif cargo_id == 2:  # Empleado
        return redirect(url_for('user_bp.Empleado.html'))
    else:
        return "Invalid Cargo"


@user_bp.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_bp.login'))

    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT nombres, email, cargo_id FROM usuarios WHERE id=%s", (user_id,))  # Verifica si la columna es 'nombres'
            user = cursor.fetchone()
            if not user:
                return "User not found"
    except Exception as e:
        return str(e)

    return render_template('Inicio.html', user=user)

@user_bp.route('/logout')
def logout():
    # Limpiar la sesión
    session.clear()
    # Redirigir al inicio de sesión
    return redirect(url_for('user_bp.login'))

@user_bp.route('/crear_user')
def crear_usuario():
    return render_template('Nuevo_Perfil.html')

@user_bp.route('/')
def home():
    return render_template('Inicio.html')  


@user_bp.route('/perfil')
def perfil():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_bp.login'))

    user = get_user_by_id(user_id)
    
    if not user:
        return "Error: Usuario no encontrado"

    return render_template('perfil.html', user=user)

def get_user_by_id(user_id):
    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            return user
    except Exception as e:
        print(f"Error al obtener el usuario: {e}")
        return None
    
@user_bp.route('/actualizar-datos', methods=['POST'])
def actualizar_datos():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_bp.login'))

    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    tipo_tarjeta = request.form['tipo-tarjeta']
    numero_tarjeta = request.form['numero-tarjeta']
    telefono = request.form['telefono']
    telefono2 = request.form['telefono2']
    direccion = request.form['direccion']
    tipo_persona = request.form['tipo-persona']

    return redirect(url_for('user_bp.perfil'))