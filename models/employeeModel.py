from flask_sqlalchemy import SQLAlchemy

from models.db import db


class EmployeeModel(db.Model):

        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100), nullable = False)
        email = db.Column(db.String(100), nullable = False)
        absence = db.Column(db.Integer, nullable = False)
        shift_duration = db.Column(db.Integer, nullable = False)
        created_at = db.Column(db.DateTime(timezone=True), nullable = False)
        start_time = db.Column(db.Time(timezone=True), nullable = False)




