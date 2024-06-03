from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length

class CreatePostForm(FlaskForm):
    title = StringField(label='Title',validators=[DataRequired(), Length(min=3, max=100)], name="title")
    content = TextAreaField(label='Content',validators=[DataRequired()], name="content")
    submit = SubmitField('Publish')
