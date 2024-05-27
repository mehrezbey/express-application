from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '449233446c37a493077f0ecf53afa01f7cb4f2ea3b1f717c6d4d1b3ad72f430c'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///express.db'

db = SQLAlchemy(app)
# To prevent circular import (routes import also app)
from express import routes

