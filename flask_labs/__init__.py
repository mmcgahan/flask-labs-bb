from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from flask.ext.babel import Babel

app = Flask(__name__)
app.config.from_object('flask_labs.defaults.Config')
app.config.from_envvar('LABS_SETTINGS')
db = SQLAlchemy(app)
babel = Babel(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "login"

import models


@login_manager.user_loader
def load_user(userid):
    return models.User.query.get(userid)

import views
import api
