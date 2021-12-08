from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from models.db import db
from sqlalchemy.sql import func


class EmployeeModel(db.Model):

        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100), nullable = False)
        email = db.Column(db.String(100), nullable = False)
        absence = db.Column(db.Integer, nullable = False)
        shift_duration = db.Column(db.Integer, nullable = False)
        #created_at = db.Column(db.DateTime(timezone=False), nullable=False, server_default=func.now())
        created_at = db.Column(db.DateTime, default=datetime.utcnow())

        start_time = db.Column(db.Time, nullable = False)