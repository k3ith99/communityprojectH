from .Config import db  #import from __init__

# each are columns of a table
# class represents a table

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(10000), nullable=False)
    address = db.Column(db.String(280))
    def __init__(self,firstname,surname,email,password,address):
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.password = password
        self.address = address


    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname, 
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'address': self.address
        }

# contains the options user can select?
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    country = db.Column(db.String(150))
    stars = db.Column(db.Integer)

# class Itinerary(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(100))
#     country = db.Column(db.String(150))
#     stars = db.Column(db.Integer)