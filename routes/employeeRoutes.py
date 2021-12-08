from flask import Flask, request
from flask_restful import Resource, reqparse, abort

from dao import userDao
from models.employeeModel import EmployeeModel

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("name", type=str, help="my naaame")
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
        userDao.create(args)