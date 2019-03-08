from flask import render_template,redirect,url_for,abort
from . import main
from ..models import Comment
from .forms import CommentForm
from .. import db


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome '
    comments=Comment.get_comments()
    
    return render_template('index.html', title = title ,comments=comments)


@main.route('/comment/new', methods=['GET', 'POST'])
def new_comment():
    form = CommentForm()
    comments=Comment.query.all()
    if form.validate_on_submit():
        comment = form.comment.data
        print(comment)
        new_comment = Comment(comment = comment)
        new_comment.save_comments()
        return redirect(url_for('main.index')) 

        db.session.add()
        db.session.commit()
 
    return render_template('new_comment.html', comment_form= form, comment=comments) 


