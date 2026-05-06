from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Crear carpeta instance si no existe
    os.makedirs(os.path.join(basedir, '..', 'instance'), exist_ok=True)

    # Configuración
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'instance', 'finanzas.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')

    # Extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    login_manager.login_message = "Tenés que iniciar sesión para acceder a esta página."
    login_manager.login_message_category = "warning"

    # Blueprints
    from .routes import main
    app.register_blueprint(main)

    # Crear DB
    with app.app_context():
        db.create_all()

    return app