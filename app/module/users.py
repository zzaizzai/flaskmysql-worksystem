from app.db import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255))
    user_pw = db.Column(db.String(255))
    department = db.Column(db.String(255))
