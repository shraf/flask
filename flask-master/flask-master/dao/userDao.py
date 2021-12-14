from flask_restful import fields, marshal_with
from models.db import db
from models.employeeModel import Employee
from models.attendenceModel import Attendence
from datetime import datetime, date
from datetime import timedelta
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'password':fields.String,
    'shift_duration': fields.Integer,
    'created_at': fields.String,
    'start_time': fields.String
}
@marshal_with(resource_fields)
def getAll():
    result =  Employee.query.all()

    for row in result:
        row.start_time=str(row.start_time)
        row.created_at=str(row.created_at)

    return result

@marshal_with(resource_fields)
def getById(id):
    result = Employee.query.get(id)
    result.start_time=str(result.start_time)
    result.created_at=str(result.created_at)
    return result

def create(user):
    db.session.add(Employee(**user))
    db.session.commit()
    return True


def update(new_user, id):
    user = Employee.query.get(id)
    if(user == None):
        return False
    user.name = new_user['name']
    db.session.commit()
    return True

def delete(id):
    user = Employee.query.get(id)
    if(user==None):
        return False
    db.session.delete(user)
    db.session.commit()
    return True

def attend(id):
    employee = Employee.query.get(id)
    if (employee == None):
        return 404
    if(employee.last_check==datetime.today().date()):
        return 409
    attendence = Attendence()
    attendence.employee_id=id
    attendence.date = datetime.now()
    curr = datetime.now().time()
    tdelta=datetime.combine(date.today(),curr)-datetime.combine(date.today(),employee.start_time)
    munites_limit = 1800
    if(tdelta.seconds>=1800):
        attendence.late = True
    employee.last_check = datetime.today()
    db.session.add(attendence)
    db.session.commit()
    return True