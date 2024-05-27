from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,EmailField,DateField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class SignupForm(FlaskForm):
    first_name = StringField(label="Fist Name",validators=[DataRequired(),Length(min=3,max=20)],name="first-name")
    last_name = StringField(label="Last Name",validators=[DataRequired(),Length(min=3,max=20)],name="last-name")
    email = EmailField('Email',validators=[DataRequired(),Email()], name="email")
    password = PasswordField('Password', validators=[DataRequired(),Length(min=10)],name="password")
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')],name="confirm-password")
    birthday  = DateField('Birthday', validators=[DataRequired()],name="birthday",format="%Y-%m-%d")
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(), Email()], name="email")
    password = PasswordField('Password', validators=[DataRequired()],name="password")
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



