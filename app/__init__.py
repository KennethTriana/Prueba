from flask import Flask
import pymysql.cursors
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Crear la conexión a la base de datos
    connection = get_db_connection()

    # Agregar la conexión a la base de datos como un atributo de la aplicación
    app.connection = connection

    # Registrar los blueprints
    from app.controllers.main_controller import main_bp
    from app.controllers.user_controller import user_bp

    app.register_blueprint(main_bp)  # Blueprint principal
    app.register_blueprint(user_bp)  # Blueprint de usuario

    # Retornar la instancia de la aplicación Flask
    return app

# Función para crear la conexión a la base de datos
def get_db_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='animales',
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None