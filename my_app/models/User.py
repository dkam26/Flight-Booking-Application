from decimal import Decimal
import datetime
from my_app import db

class User(db.Model):
    """Table for users"""
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    surname = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    user_type = db.Column(db.String(255))
    def __init__(self, username, surname, firstname , email, password, profile_picture,user_type):
        self.username = username
        self.surname = surname
        self.firstname = firstname
        self.email = email
        self.password = password
        self.profile_picture = profile_picture
        self.user_type = user_type
