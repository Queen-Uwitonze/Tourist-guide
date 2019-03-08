from . import main
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from ..models import  Map,Site
from flask_googlemaps import Map

app = Flask(__name__, template_folder=".")
GoogleMaps(app)

@main.route("/")
def sitesview():

    title="Nices places to visit in Rwanda"
    return render_template('category.html', title=title)



@main.route("/map")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('maps.html', mymap=mymap, sndmap=sndmap)



@main.route('/Volcanos')
def Volcanos():
  
    Volcanos_sites = Site.query.filter_by(category='Volcanos').all()

    return render_template('volcanos.html', Volcanos=Volcanos_sites)

@main.route('/Akagera')
def Akagera():
  
    Akagera_sites = Site.query.filter_by(category='Akagera').all()

    return render_template('akagera.html', Akagera=Akagera_sites)


@main.route('/Royal')
def Royal():
    Royal_sites = Site.query.filter_by(category='Royal').all()
    return render_template('royal.html', Royal=Royal_sites)
    
@main.route('/Nyungwe')
def Nyungwe():
    Nyungwe_sites = Site.query.filter_by(category='Nyungwe').all()
    return render_template('nyungwe.html', Nyungwe=Nyungwe_sites)

@main.route('/Kivu')
def Kivu():
    Kivu_sites = Site.query.filter_by(category='Kivu').all()
    return render_template('kivu.html', Kivu=Kivu_sites)

@main.route('/Gisuma')
def Gisuma():
    Gisuma_sites = Site.query.filter_by(category='Gisuma').all()
    return render_template('gisuma.html', Gisuma=Gisuma_sites)

@main.route('/Gishwati')
def Gishwati():
    Gishwati_sites = Site.query.filter_by(category='Gishwati').all()
    return render_template('gishwati.html', Gishwati=Gishwati_sites)

























# @main.route('/site-location', methods=['GET', 'POST'])
# def get_site_location():
#     form = SiteForm()
    
#     if sites_form.validate_on_submit():
#         title = sites_form.title.data
#         content  = sites_form.content.data
#         username  = sites_form.username.data
#         category = sites_form.category.data
#         upvote = sites_form.category.data
#         user_id = sites_form.user_id.data
#         new_sites = Site(title=title,content=content,category=category,user_id=current_user.id)
#         new_sites.save_sites() 
    
#         return redirect(url_for('main.index'))

#     return render_template('new_sites.html', sites_form=sites_form)