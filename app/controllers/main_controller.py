from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return render_template('Inicio.html')  

@main_bp.route('/crear_user')
def crear_usuario():
    return render_template ('Nuevo_Perfil.html')