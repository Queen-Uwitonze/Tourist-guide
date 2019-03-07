import flask
from flask import request, url_for, render_template, redirect
from . import main
from ..models import  Map,Site


@main.route('/',methods=['GET','POST'])
def my_maps():

  mapbox_access_token = 'AIzaSyAt9PFcZklUveOfa6E7KYzLYLSQvGGfmqw'
  title="Tour app"
  return render_template('map.html',title=title,mapbox_access_token=mapbox_access_token)

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
    return render_template('map.html', Kivu=Kivu_sites)

@main.route('/Gisuma')
def Gisuma():
    Gisuma_sites = Site.query.filter_by(category='Gisuma').all()
    return render_template('map.html', Gisuma=Gisuma_sites)

@main.route('/Gishwati')
def Gishwati():
    Gishwati_sites = Site.query.filter_by(category='Gishwati').all()
    return render_template('map.html', Gishwati=Gishwati_sites)

@main.route('/Kibuye')
def Kibuye():
    Kibuye_sites = Site.query.filter_by(category='Kibuye').all()
    return render_template('map.html', Kibuye=Kibuye_sites)

























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