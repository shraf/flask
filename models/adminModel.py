from flask_sqlalchemy import SQLAlchemy

from models.db import db


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(300), nullable=False)
