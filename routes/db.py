from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
db = SQLAlchemy()

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    sdt = db.Column(db.String)
    email = db.Column(db.String)
    songuoi = db.Column(db.Integer)
    soban = db.Column(db.String)
    ngaybook = db.Column(db.Date)
    giobook = db.Column(db.Time)
    nhahang = db.Column(db.String)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)


class Config:
    SECRET_KEY = 'n9b9monkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///booking_restaurant.db'
    PERMANENT_SESSION_LIFETIME =  timedelta(days=30)