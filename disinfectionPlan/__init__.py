from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Developement")
db = SQLAlchemy(app)


from .dinsinfection_app.app import app_bp
app.register_blueprint(app_bp)