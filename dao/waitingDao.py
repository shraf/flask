from flask_restful import fields, marshal_with
from models.db import db
from models.waitingModel import Waiting

resource_fields = {
    'id': fields.Integer,
    'created_at': fields.DateTime
}


@marshal_with(resource_fields)
def getAll():
    result = WaitingModel.query.all()
    return result


@marshal_with(resource_fields)
def getById(id):
    result = WaitingModel.query.get(id)
    print(result)
    return result


def create(waiting_employee):
    db.session.add(WaitingModel(**waiting_employee))
    db.session.commit()
    return True