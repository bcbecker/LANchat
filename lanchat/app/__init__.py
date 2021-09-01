from flask import Flask


def create_app():
    """Constructs the core flask app"""
    
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    with app.app_context():
        # Imports
        from .views import view
        from .database import DataBase

        # Routes
        app.register_blueprint(view, url_prefix="/")

        return app