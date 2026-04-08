from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuración básica
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finanzas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'clave-secreta'  # cámbiala por algo seguro

    # Inicializamos extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Mensaje elegante en lugar del feo por defecto
    login_manager.login_message = "Tenés que iniciar sesión para acceder a esta página."
    login_manager.login_message_category = "warning"

    # Registramos blueprint
    from .routes import main
    app.register_blueprint(main)

    # Crear tablas si no existen
    with app.app_context():
        db.create_all()

    return app