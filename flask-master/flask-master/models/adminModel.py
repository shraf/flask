from flask_sqlalchemy import SQLAlchemy

from models.db import db



class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password= db.Column(db.String(300), nullable = False)