from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from models.db import db
from sqlalchemy.sql import func


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    active = db.Column(db.Boolean, default=False)
    shift_duration = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    start_time = db.Column(db.Time, nullable=True)
    last_check_in = db.Column(db.Date, default=datetime(1, 1, 1))
    last_check_out=db.Column(db.Date, default=datetime(1, 1, 1))
    attendance = relationship("Attendance")
    attended_days = db.Column(db.Integer, default=0)
    attended_late = db.Column(db.Integer, default=0)
    salary = db.Column(db.Integer,default=0)
    gender=db.Column(db.String(10),nullable=False)
    phone=db.Column(db.String(100),nullable=False)

    def __init__(self, id, name, email, password, active, shift_duration, start_time,salary,gender,phone,
                 attendance=[]):
        self.attendance = attendance
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.shift_duration = shift_duration
        self.start_time = start_time
        self.salary=salary
        self.gender=gender
        self.phone=phone
