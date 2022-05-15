from flask import render_template, request
from . import main
from ..requests import get_quote, get_quotes
from ..models import Quote
from .forms import CommentForm
from flask_login import login_required



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