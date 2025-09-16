from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User accounts
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # store hashed passwords
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Rental listings saved to DB
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(20))
    link = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # optional, link to user
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Alerts (could be email notifications)
class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'))
    sent = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
