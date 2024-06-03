import os

class Config : 
    SECRET_KEY= os.environ.get('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI= os.environ.get('SQLITE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS= True
    MAIL_USERNAME= os.environ.get('EMAIL_USER')
    MAIL_PASSWORD= os.environ.get('PASSWORD_USER_PYTHON')
    MAIL_USE_SSL= False
    TESTING= False