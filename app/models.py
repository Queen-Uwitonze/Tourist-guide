from . import db
class Site(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'site',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'site',lazy="dynamic")
   
    def __repr__(self):
        return f'Site {self.name}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    site_id = db.Column(db.Integer,db.ForeignKey('sites.id'))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls):
        comments = Comment.query.all()
        return comments   


    @classmethod
    def new_comment(cls,id):
        comments = Comment.query.all()
        return comments   


    def __repr__(self):
        return f'Site {self.comment}' 

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer,primary_key = True)
    rate = db.Column(db.Integer())  
    site_id = db.Column(db.Integer,db.ForeignKey('sites.id'))


    def save_review(self):
       db.session.add(self)
       db.session.commit() 
  
