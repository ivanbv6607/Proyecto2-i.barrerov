from flask import Flask, render_template
from app.config.db import db
from app.config.config import Config
from app.config.routes import register_routes
from app.config.auth import login_manager

def create_app(config):
        app = Flask(__name__, template_folder="views")

        app.config.from_object(Config)
        db.init_app(app)
        login_manager.init_app(app)
        register_routes(app)

        with app.app_context():
                db.create_all()
        return app
        app.config["SECRET_KEY"] = SEC_KEY
        """if __name__ == "__main__":
                app.run(debug=True)""" 
