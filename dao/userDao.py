from flask_restful import fields, marshal_with
from models.db import db
from models.employeeModel import Employee
from models.attendenceModel import Attendance
from datetime import datetime, date

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'password': fields.String,
    'shift_duration': fields.Integer,
    'created_at': fields.String,
    'start_time': fields.String,
    'attendance': fields.List(fields.Nested({
        "id": fields.Integer,
        "date": fields.DateTime
    })),
    'attended_days': fields.Integer,
    'attended_late': fields.Integer,
    'salary':fields.Integer,
    'gender':fields.String,
    'phone':fields.String,
    'active':fields.Boolean
}


@marshal_with(resource_fields)
def get_all():
    result = Employee.query.all()

    for row in result:
        row.start_time = str(row.start_time)
        row.created_at = str(row.created_at)

    return result


@marshal_with(resource_fields)
def get_by_id(id):
    result = Employee.query.get(id)
    if result is None:
        return result
    else:
        if result.id !=0:
            if result.start_time is not None:
               result.start_time = str(result.start_time)
            if result.created_at is not None:
               result.created_at = str(result.created_at)

    return result

@marshal_with(resource_fields)
def get_by_active(is_active):
    results=Employee.query.filter_by(active=is_active).all()

    for result in results:
        result.start_time = str(result.start_time)
        result.created_at = str(result.created_at)
    return results
def create(user):
    employee= Employee(**user)
    db.session.add(employee)
    db.session.commit()
    return employee.id


def update(new_user, id):
    user = Employee.query.get(id)
    if user is None:
        return False
    for key, value in new_user.items():
        if value is not None:
            setattr(user, key, value)
    db.session.commit()
    return True


def delete(id):
    user = Employee.query.get(id)
    if user is None:
        return False
    db.session.delete(user)
    db.session.commit()
    return True


# attendance function
def attend(id):
    # get the employee with the id sent it should be the entered fingerprint
    employee = Employee.query.get(id)
    # check if the employee exist
    if employee is None or not employee.active:
        return 404
    # check if th employee already checked out today
    if employee.last_check_out == datetime.today().date():
        return 409
    # check if the employee checked in and didn't check out
    if employee.last_check_in == datetime.today().date() and employee.last_check_out != datetime.today().date():
        curr = datetime.now().time()
        time_delta = datetime.combine(date.today(), curr) - datetime.combine(date.today(), employee.start_time)
        # check if the employee checking out after the shift duration
        if time_delta.seconds >= employee.shift_duration * 60 * 60:
            attendance = Attendance()
            attendance.employee_id = id
            attendance.date = datetime.now()
            employee.last_check_out = datetime.today()
            db.session.add(attendance)
            db.session.commit()
            return True
        else:
            return "Can only check after finishing the shift !"

    # the employee didn't check in
    else:
        attendance = Attendance()
        attendance.employee_id = id
        attendance.date = datetime.now()
        curr = datetime.now().time()
        time_delta = datetime.combine(date.today(), curr) - datetime.combine(date.today(), employee.start_time)
        late_seconds_limit = 1800
        attend_seconds_limit = 3600
        # check if the employee is so late that we don't check him this day
        if time_delta.seconds >= attend_seconds_limit:
            return "employee reached late limit"
        # if the employee is barely late that he should be  checked late
        elif time_delta.seconds >= late_seconds_limit:
            employee.attended_late += 1
        # if the employee is not late at all
        elif time_delta.seconds < late_seconds_limit:
            employee.attended_days += 1

        employee.last_check_in = datetime.today()
        db.session.add(attendance)
        db.session.commit()
        return True
