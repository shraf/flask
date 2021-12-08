from flask_restful import fields, marshal_with
from models.db import db
from models.employeeModel import EmployeeModel

resource_fields = {
    'id' : fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'absence' : fields.Integer,
    'shift_duration': fields.Integer,
    'created_at': fields.DateTime,
    'start_time': fields.DateTime
}
@marshal_with(resource_fields)
def getAll():
    result =  EmployeeModel.query.all()
    return result

@marshal_with(resource_fields)
def getById(id):
    result = EmployeeModel.query.get(id)
    print(result)
    return result

def create(user):
    db.session.add(EmployeeModel(**user))
    db.session.commit()
    return True


def update(new_user, id):
    user = EmployeeModel.query.get(id)
    if(user == None):
        return False
    user.name = new_user['name']
    db.session.commit()
    return True

def delete(id):
    user = EmployeeModel.query.get(id)
    if(user==None):
        return False
    db.session.delete(user)
    db.session.commit()
    return True