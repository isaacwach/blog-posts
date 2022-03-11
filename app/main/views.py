from flask import render_template, redirect, request, url_for, abort
from . import main 
from flask_login import login_required, current_user
from .. import db,photos
from .forms import ProfileUpdate,PitchForm,CommentForm
from ..models import User,Pitch,Comment,Upvote,Downvote

@main.route('/')
def index():
    blogs = Blog.query.all()
    politics = Blog.query.filter_by(category = 'Politics').all() 
    sports = Blog.query.filter_by(category = 'Sports').all()
    celebrity = blog.query.filter_by(category = 'Celebrity-gossip').all()

    return render_template('index.html', pitches=pitches, politics=politics, sports=sports, celebrity=celebrity)
    
@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_blog():
    form = BlogForm(request.form)
    if form.validate_on_submit():
        title = form.title.data
        user_id = current_user
        category = form.category.data
        post = form.post.data
        
        new_blog_object = Blog(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_blog_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('post_blog.html', form = form)
