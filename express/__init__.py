from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from express.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.log_in'
login_manager.login_message_category ='info'

mail = Mail()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from express.main.routes import main
    from express.users.routes import users
    from express.posts.routes import posts
    from express.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    return app
