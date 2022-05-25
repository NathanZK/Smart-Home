from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Room(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    temp = db.Column(db.Boolean, default=False)
    humid = db.Column(db.Boolean, default=False)
    lock = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
       return f"Room('{self.name}','{self.temp}', '{self.humid}','{self.lock}')"


class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    rooms = db.relationship('Room')

    def __repr__(self):
       return f"User('{self.first_name}')"
    