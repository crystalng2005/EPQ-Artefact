import openai
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

openai.api_key = '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'

app = Flask(__name__)
app.config['SECRET_KEY'] = '433ca33a3bffb16ca5bfb7563fb05ab6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from flaskblog import routes