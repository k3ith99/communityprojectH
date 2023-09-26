from . import db  #import from __init__

# each are columns of a table
# class represents a table

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(280))