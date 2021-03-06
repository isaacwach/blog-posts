from flask import render_template, redirect, request, url_for, abort
from . import main 
from flask_login import login_required, current_user
from .. import db,photos
from .forms import ProfileUpdate,BlogForm,CommentForm
from ..models import User,Blog,Comment,Upvote,Downvote
from ..requests import get_quotes 

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # title= "Zacs trendy news app"
    quotes= get_quotes()
    return render_template('index.html', quotes=quotes)

@main.route('/blogs')
def blogs():
    blogs = Blog.query.all()
    politics = Blog.query.filter_by(category = 'Politics').all() 
    sports = Blog.query.filter_by(category = 'Sports').all()
    celebrity = Blog.query.filter_by(category = 'Celebrity-gossip').all()

    return render_template('blogs.html', blogs=blogs, politics=politics, sports=sports, celebrity=celebrity)
    
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

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)

@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_c()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html', form =form, blog = blog, all_comments=all_comments)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_blogs = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for blog in get_blogs:
        to_str = f'{blog}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, blog_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    blog = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for b in blog:
        to_str = f'{b}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, blog_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))
