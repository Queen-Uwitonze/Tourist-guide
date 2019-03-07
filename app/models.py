from . import db

class Map(db.Model):

    __tablename__ = 'maps'

    id = db.Column(db.Integer,primary_key = True)
    places = db.Column(db.String(255))
    sites = db.relationship('Site',backref = 'site',lazy="dynamic")

    def save_maps(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_maps(id):
        maps = Map.query.filter_by(id=maps_id).all()
        return maps

    def __repr__(self):
        return f'User {self.name}'


class Site(db.Model):
  __tablename__ = 'sites'
  
  id = db.Column(db.Integer,primary_key = True)
  location_name = db.Column(db.String(255))
  category = db.Column(db.String(255))
  images= db.Column(db.String(225))
  maps_id = db.Column(db.Integer,db.ForeignKey('maps.id'))
  
  def save_sites(self):
      db.session.add(self)
      db.session.commit()

  @classmethod
  def get_site_location(id):
      sites = Site.query.filter_by(id=sites_id).all()
      return sites

  def __repr__(self):
      return f'User {self.name}'