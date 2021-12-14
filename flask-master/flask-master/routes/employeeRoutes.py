from flask import Flask, request
from flask_restful import Resource, reqparse, abort
import flask_bcrypt
from dao import userDao
from models.employeeModel import Employee
from flask_restful import inputs
import datetime

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("id", type=int, help="id")
user_put_args.add_argument("name", type=str, help="name")
user_put_args.add_argument("email", type=str, help="email")
user_put_args.add_argument("password", type=str, help="password")
user_put_args.add_argument("shift_duration", type=int, help="shift_duration")
user_put_args.add_argument("start_time", type=str, help="start_time")

class EmployeeRouter (Resource):

    def get(self, id):
        result = userDao.getById(id)
        if(result["id"]==0):
            abort(404)
        return result
    def patch(self, id):
        args = user_put_args.parse_args()
        if(userDao.update(args,id)==False):
            abort(404)
        return {"data":"success"}

    def delete(self, id):
        if(userDao.delete(id)==False):
            abort(404)
        return {"data":"success"}

class AttendenceRouter(Resource):
    def post(self,id):
        res = userDao.attend(id)
        if ( res == True):
            return {"data": "success"}
        abort(res)
class EmployeeListRouter(Resource):
    def get(self):
        return userDao.getAll()
    def post(self):
        args = user_put_args.parse_args()
        args['start_time']=datetime.datetime.strptime(args['start_time'], '%H::%M::%S').time()
        args['password']=flask_bcrypt.generate_password_hash(args['password']).decode('utf8')
        userDao.create(args)

class EmployeeLoginRouter(Resource):
    def post(self):
        args = user_put_args.parse_args()
        employee=Employee.query.filter_by(email=args['email']).first()
        if not employee:
            print("m4 hna")
            return 'User does not exist', 404
        if flask_bcrypt.check_password_hash(employee.password , args['password']):
            return f'Welcome back {employee.name} Your attendance days are {employee.attendence}'
        else:
            return 'wrong password!'