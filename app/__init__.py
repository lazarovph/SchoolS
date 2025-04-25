from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('instance.config')  # Задаване на конфигурацията
    
    db.init_app(app)
    migrate.init_app(app, db)  # Инициализиране на Flask-Migrate

    from . import routes  # Импортиране на маршрути
    app.register_blueprint(routes.bp)

    return app
