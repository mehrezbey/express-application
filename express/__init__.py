from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


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
# To prevent circular import (routes import also app)
from express import routes

