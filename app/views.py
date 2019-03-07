from flask import render_template
from app import app

# Views
@app.route('/')
def reservation():

    title = 'Hotels in Rwanda'
    return render_template('reservation.html',title = title)

@app.route('/transport') 
def transport():


    return render_template('transport.html')