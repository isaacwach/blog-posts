from flask import render_template, redirect, request, url_for, abort
from . import main 
from flask_login import login_required, current_user
from .. import db,photos
from .forms import ProfileUpdate,PitchForm,CommentForm
from ..models import User,Pitch,Comment,Upvote,Downvote

@main.route('/')
def index():
    pitches = Pitch.query.all()
    motivation = Pitch.query.filter_by(category = 'Motivation').all() 
    jokes = Pitch.query.filter_by(category = 'Jokes').all()
    education = Pitch.query.filter_by(category = 'Education').all()

    return render_template('index.html', pitches=pitches, education=education, motivation=motivation, jokes=jokes)
    
