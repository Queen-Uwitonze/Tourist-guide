from flask import render_template,request,redirect,url_for
from . import main



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    

    title = 'Homepage-Touristic Guide App'
   

    return render_template('Home.html',title = title)




