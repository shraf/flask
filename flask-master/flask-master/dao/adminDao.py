from flask_restful import fields, marshal_with
from models.db import db
from models.adminModel import Admin
resource_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
}
@marshal_with(resource_fields)
def getAll():
    result = Admin.query.all()
    return result
def create(user):
    db.session.add(Admin(**user))
    db.session.commit()
    return True