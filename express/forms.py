from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,EmailField,DateField,SubmitField,BooleanField,FileField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from express.models import User

class SignupForm(FlaskForm):
    first_name = StringField(label="Fist Name",validators=[DataRequired(),Length(min=3,max=20)],name="first-name")
    last_name = StringField(label="Last Name",validators=[DataRequired(),Length(min=3,max=20)],name="last-name")
    email = EmailField('Email',validators=[DataRequired(),Email()], name="email")
    password = PasswordField('Password', validators=[DataRequired(),Length(min=10)],name="password")
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')],name="confirm-password")
    birthday  = DateField('Birthday', validators=[DataRequired()],name="birthday",format="%Y-%m-%d")
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(), Email()], name="email")
    password = PasswordField('Password', validators=[DataRequired()],name="password")
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField(label='First name',validators=[DataRequired(), Length(min=2, max=20)], name="first-name")
    last_name = StringField(label='Last name',validators=[DataRequired(), Length(min=2, max=20)], name="last-name")
    email = EmailField('Email',validators=[DataRequired(), Email()], name="email")
    picture = FileField("Profile Picture",validators=[FileAllowed(['jpg','png'])])
    birthday  = DateField('Birthday', validators=[DataRequired()],name="birthday",format="%Y-%m-%d")

    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class CreatePostForm(FlaskForm):
    title = StringField(label='Title',validators=[DataRequired(), Length(min=3, max=100)], name="title")
    content = TextAreaField(label='Content',validators=[DataRequired()], name="content")
    submit = SubmitField('Publish')

class ResetPasswordRequestForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(),Email()], name="email")
    submit = SubmitField('Send')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('That email does not exist. Please register first!')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(),Length(min=10)],name="password")
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')],name="confirm-password")
    submit = SubmitField('Reset Password')


