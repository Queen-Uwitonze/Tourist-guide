from . import db


class Accomodation(db.model):
    __tablename__="accomodations"

    id = db.Column(db.Integer,primary_key = True)
    hotelname = db.Column(db.String(250))
    hotelroom = db.Column(db.String(250))
    calendar = db.Column(db.Integer(250))
    email = db.Column(db.String(255),unique = True,index = True)

    def save_accommodation(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_accommodation(id):
        accommodations = Accomodation.query.all()
        return accommodations

    def __repr__(self):
        return f'User {self.name}'

class Transport(db.model):
    __tablename__="transports"

    id = db.Column(db.Integer,primary_key = True)
    car = db.Column(db.String(250))
    flight = db.Column(db.String(250))
    email = db.Column(db.String(255),unique = True,index = True)
