from app import db
from datetime import date

class User(db.Model):
    __tablename__ = 'user_deets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

    contacts = db.relationship('Contact', backref='user', lazy=True)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_deets.id'), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(20), nullable=False)
    event_date = db.Column(db.Date, nullable=False)

    def is_today(self):
        today = date.today()
        return self.event_date.day == today.day and self.event_date.month == today.month