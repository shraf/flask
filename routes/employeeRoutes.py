from flask import Flask, request
from flask_restful import Resource, reqparse, abort

from dao import userDao
from models.employeeModel import EmployeeModel
from flask_restful import inputs
import datetime

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("id", type=int, help="id")
user_put_args.add_argument("name", type=str, help="name")
user_put_args.add_argument("email", type=str, help="email")
user_put_args.add_argument("absence", type=int, help="absence")
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
class EmployeeListRouter(Resource):
    def get(self):
        return userDao.getAll()
    def post(self):
        args = user_put_args.parse_args()
        args['start_time']=datetime.datetime.strptime(args['start_time'], '%H::%M::%S').time()
        userDao.create(args)
    def put(self):
        print("")