from flask_restful import fields, marshal_with
from models.db import db
from models.waitingModel import Waiting

resource_fields = {
    'id': fields.Integer,
    'created_at': fields.DateTime
}


@marshal_with(resource_fields)
def get_all():
    result = Waiting.query.all()
    return result


@marshal_with(resource_fields)
def get_by_id(id):
    result = Waiting.query.get(id)
    return result


def create(waiting_employee):
    db.session.add(Waiting(**waiting_employee))
    db.session.commit()
    return True

def delete(id):
    user = Waiting.query.get(id)
    if user is None:
        return False
    db.session.delete(user)
    db.session.commit()
    return True