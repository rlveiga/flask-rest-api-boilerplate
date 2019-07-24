from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config import config 

# db = SQLAlchemy()

# set config object as parameter for create_app function
def create_app():
	app = Flask(__name__)

	# attach app to db variable with init_app function

	# register blueprints
	from .main import main as main_blueprint

	app.register_blueprint(main_blueprint)

	return app