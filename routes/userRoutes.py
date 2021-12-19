from flask import Flask, request
from flask_restful import Resource, reqparse, abort

from dao import userDao
from models.userModel import UserModel

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("name", type=str, help="my naaame")


class UserRouter(Resource):
    def get(self, id):
        result = userDao.get_by_id(id)
        if result["id"] == 0:
            abort(404)
        return result

    def patch(self, id):
        args = user_put_args.parse_args()
        if not userDao.update(args, id):
            abort(404)
        return {"data": "success"}

    def delete(self, id):
        if not userDao.delete(id):
            abort(404)
        return {"data": "success"}


class UserListRouter(Resource):
    def get(self):
        return userDao.get_all()

    def post(self):
        args = user_put_args.parse_args()
        userDao.create(args)
