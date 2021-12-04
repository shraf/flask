from flask_restful import fields, marshal_with
from models.db import db
from models.userModel import UserModel

resource_fields = {
    'id' : fields.Integer,
    'name': fields.String
}
@marshal_with(resource_fields)
def getAll():
    result =  UserModel.query.all()
    return result

@marshal_with(resource_fields)
def getById(id):
    result = UserModel.query.get(id)
    print(result)
    return result

def create(user):
    db.session.add(UserModel(**user))
    db.session.commit()
    return True


def update(new_user, id):
    user = UserModel.query.get(id)
    if(user == None):
        return False
    user.name = new_user['name']
    db.session.commit()
    return True

def delete(id):
    user = UserModel.query.get(id)
    if(user==None):
        return False
    db.session.delete(user)
    db.session.commit()
    return True