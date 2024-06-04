from dataclasses import dataclass, field
from datetime import date, datetime
from express import db ,login_manager
from flask_login import UserMixin, current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
import secrets
import re


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@dataclass
class User(db.Model,UserMixin):
    __table_name__= "user"
    
    id:int= field(init=False, repr=False)
    firstname:str 
    lastname:str 
    username:str= field(init=False, repr=False)
    email:str 
    image_file:str
    password:str =  field(repr=False)
    birthday:date
    first_date:date
    # posts:object= field(init=False, repr=False)

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20),  nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    birthday = db.Column(db.DateTime , nullable = True)
    first_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)

    def add_user(self):
        username = re.sub(r'\W+', '', self.firstname).lower()+"_"+ re.sub(r'\W+', '', self.lastname).lower()+"_"+secrets.token_urlsafe(8)
        user = User.query.filter_by(username = username).first()
        while(user):
            username = re.sub(r'\W+', '', self.firstname).lower()+"_"+ re.sub(r'\W+', '', self.lastname).lower()+"_"+secrets.token_urlsafe(8)
        self.username = username
        db.session.add(self)
        db.session.commit()

    def get_reset_token(self, expires_time = 1800):
        s = Serializer(current_app.config['SECRET_KEY'],expires_time)
        return s.dumps({'user_id' :  self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    

@dataclass
class Post(db.Model):
    id:int= field(init=False, repr=False)
    title:str
    date_posted:date = field(init=False)
    content:str = field(repr=False)
    user_id:int = field(repr=False)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def create_post(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def posts_published():
        posts_number = db.session.query(Post).filter_by(author=current_user).count()
        return posts_number
    