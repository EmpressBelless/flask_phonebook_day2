from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#initilize our login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = 'you are not authorized. you should log in'
login_manager.login_message_category = 'danger'

from app import routes, models

