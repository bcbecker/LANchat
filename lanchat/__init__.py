from flask import Flask
from lanchat.config import Config


def create_app():
    """Constructs the core flask app"""
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    with app.app_context():
        # Imports
        from .routes import main

        # Routes
        app.register_blueprint(main, url_prefix="/")

        return app