from dataclasses import dataclass, field
from datetime import date, datetime
from express import db 


@dataclass
class User(db.Model):
    __table_name__= "user"
    
    id:int= field(init=False, repr=False)
    firstname:str 
    lastname:str 
    email:str 
    image_file:str
    password:str =  field(repr=False)
    birthday:date
    # posts:object= field(init=False, repr=False)

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20),  nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    birthday = db.Column(db.DateTime , nullable = True)
    posts = db.relationship('Post', backref='author', lazy=True)

    # def add_user(self):
    #     db.session.add(self)
    #     db.session.commit()

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
# db.create_all()