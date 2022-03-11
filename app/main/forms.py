from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, TextAreaField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Email
from ..models import User

class ProfileUpdate(FlaskForm):
    profile_bio=TextAreaField('Tell us about yourself.', validators=[DataRequired()])
    submit=SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')

class PitchForm(FlaskForm):
    title=TextAreaField('Title', validators=[DataRequired()])
    category=SelectMultipleField('Select Category', choices=[('Politics', 'Politics'), ('Sports', 'Sports'), ('Celebrity-gossip', 'Celebrity-gossip')], validators=[DataRequired()])
    post= TextAreaField('Enter your blog', validators=[DataRequired()])
    submit=SubmitField('Create')