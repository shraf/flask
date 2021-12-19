from flask import Flask, request
from flask_restful import Resource, reqparse, abort
import flask_bcrypt
from dao import userDao,waitingDao
from models.employeeModel import Employee
from flask_restful import inputs
import datetime
import jwt

request_payload = reqparse.RequestParser()
request_payload.add_argument("id", type=int, help="fingerprint id")
request_payload.add_argument("name", type=str, help="employee name")
request_payload.add_argument("email", type=str, help="employee email")
request_payload.add_argument("password", type=str, help="employee password")
request_payload.add_argument("shift_duration", type=int, help="shift duration in hours")
request_payload.add_argument("start_time", type=str, help="start time of the shift")
request_payload.add_argument("active", type=bool, help="is the user activated")
request_payload.add_argument("salary", type=int, help="salary of the employee")
request_payload.add_argument("gender", type=str, help="gender of the employee")
request_payload.add_argument("phone", type=str, help="employee phone number")

class EmployeeRouter(Resource):

    def get(self, id):
        result = userDao.get_by_id(id)
        token = request.headers.get("authorization")
        decoded_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        if result["id"] == 0:
            abort(404)
        if decoded_token["type"] != "admin" :
            abort(403)
            if decoded_token['id'] != result['id']:
                abort(403)
        del result['password']
        return result


    def patch(self, id):
        args = request_payload.parse_args()
        token = request.headers.get("authorization")
        decoded_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        if decoded_token["type"] != "admin":
            abort(403)
        if args['start_time'] is not None:
            args['start_time'] = datetime.datetime.strptime(args['start_time'], '%H::%M::%S').time()
        if args['password'] is not None:
            args['password'] = flask_bcrypt.generate_password_hash(args['password']).decode('utf8')
        if args['active']:
            waitingDao.delete(args['id'])
        if not userDao.update(args, id):
            abort(404)
        return {"data": "success"}

    def delete(self, id):
        token = request.headers.get("authorization")
        decoded_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        if decoded_token["type"] != "admin":
            abort(403)
        if not userDao.delete(id):
            abort(404)
        return {"data": "success"}


class AttendanceRouter(Resource):
    def post(self, id):
        res = userDao.attend(id)
        if res:
            return {"data": "success"}
        abort(res)


class EmployeeListRouter(Resource):
    def get(self):
        token = request.headers.get("authorization")
        decoded_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        if decoded_token["type"] == "admin":

            isActive=request.args.get('active',default=2)
            isActive=int(isActive)
            if isActive==0:
                print("xd")
                return userDao.get_by_active(False)
            elif isActive==1:
                return userDao.get_by_active(True)
            elif isActive==2:
                return userDao.get_all()
            return userDao.get_all()
        elif decoded_token["type"] == "user":
            result = userDao.get_by_id(decoded_token['id'])
            return result
        else:
            abort(403)

    def post(self):
        args = request_payload.parse_args()
        #if waitingDao.get_by_id(args['id']) == None:
        #    abort(404 )
        args['start_time'] = datetime.datetime.strptime('00::00::00', '%H::%M::%S').time()
        args['password'] = flask_bcrypt.generate_password_hash(args['password']).decode('utf8')
        args['active'] = False
        args['salary']=0
        args['shift_duration']=0
        id=userDao.create(args)
        return id


class EmployeeLoginRouter(Resource):
    def post(self):
        args = request_payload.parse_args()
        employee = Employee.query.filter_by(email=args['email']).first()
        if not employee:
            return 'User does not exist', 404
        if flask_bcrypt.check_password_hash(employee.password, args['password']):
            encoded_jwt = jwt.encode({"email": employee.email, "id": employee.id, "type": "user"}, "secret",
                                     algorithm="HS256")

            return {"jwt": encoded_jwt.decode('utf-8')}
        else:
            return 'wrong password!'

class exist(Resource):
    def get(self,id):
        result=userDao.get_by_id(id)
        if result["id"] == 0:
            return False
        else:
            return True