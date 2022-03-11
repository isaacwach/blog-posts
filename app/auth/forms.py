from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Enter Email Address', validators=[DataRequired(),Email()])
    username = StringField('Enter Your Username', validators=[DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("Email already in use")
    
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("The username already taken")

class LoginForm(FlaskForm):
    username = StringField('Your Username',validators=[DataRequired()])
    password = PasswordField('Your Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')