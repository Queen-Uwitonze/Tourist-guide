from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_googlemaps import GoogleMaps
  

bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app(config_name):

    app = Flask(__name__,instance_relative_config = True)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['GOOGLEMAPS_KEY'] = "AIzaSyAt9PFcZklUveOfa6E7KYzLYLSQvGGfmqw"

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)
    db.init_app(app)

    # you can also pass the key here if you prefer
    GoogleMaps(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Will add the views and forms
    # from app import views
    # from app import error
    return app