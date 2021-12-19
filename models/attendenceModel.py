from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from models.db import db
from sqlalchemy.sql import func


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
