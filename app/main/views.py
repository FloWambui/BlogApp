from flask import render_template,request,redirect,url_for,abort,flash,session
from . import main
from ..requests import get_quote, get_quotes
from ..models import Quote,User
from .forms import CommentForm, UpdateProfile
from flask_login import login_required
from .. import db



# Views
@main.route('/')
def index():
 
    
    quote=get_quote('random')
    title = 'BlogApp | Create Your Own Story'
    return render_template('index.html', title=title,quote=quote)

@main.route('/quotes')
def quotes():
 
    popular_quotes = get_quotes('popular')
    return render_template('quotes.html',popular = popular_quotes)

@main.route('/loggedin')
def loggedin():
    return render_template('login.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)