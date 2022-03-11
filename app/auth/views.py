from flask import render_template,url_for,flash,redirect,request
from . import auth
from ..models import User
from .. import db
from flask_login import login_user,login_required,logout_user
from .forms import RegistrationForm,LoginForm

from ..email import mail_message

@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        #print(user.email)
        #mail_message("Welcome to Spicy pitches","email/welcome_user",user.email,user=user)
        return redirect(url_for('main.index'))
    return render_template('auth/signup.html', reg_form = form)