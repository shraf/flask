from models.db import db
from sqlalchemy.sql import func


class Waiting(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
