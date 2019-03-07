from flask import render_template
from app import app

# Views
@app.route('/')
def reservation():

    title = 'Hotels in Rwanda'
    return render_template('reservation.html',title = title)

@app.route('/accommodation') 
def accommodation(id):


    return render_template('accommodation.html')