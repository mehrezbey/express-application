from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '449233446c37a493077f0ecf53afa01f7cb4f2ea3b1f717c6d4d1b3ad72f430c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Create the database tables
# with app.app_context():
#     from express.models import Post,User
#     db.create_all()

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'log_in'
login_manager.login_message_category ='info'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD_USER_PYTHON')
app.config['MAIL_USE_SSL'] = False
app.config['TESTING'] = False

mail = Mail(app)
# To prevent circular import (routes import also app)
from express import routes

