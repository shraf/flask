import flask_bcrypt
from flask import Flask, request
from flask_restful import Resource, reqparse, abort
from dao import adminDao
from models.adminModel import Admin
from flask_restful import inputs
from flask_bcrypt import Bcrypt
import jwt

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("id", type=int, help="id")
user_put_args.add_argument("username", type=str, help="username")
user_put_args.add_argument("password", type=str, help="password")


class AdminRegisterRouter(Resource):
    def get(self):
        token = request.headers.get("authorization")
        decoded_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        if decoded_token["type"] != "admin":
            abort(403)
        return adminDao.get_all()

    def post(self):
        token = request.headers.get("authorization")
        decoded_token = jwt.decode(token, 'secret', algorithms=["HS256"])
        if decoded_token["type"] != "admin":
            abort(403)
        args = user_put_args.parse_args()
        args['password'] = flask_bcrypt.generate_password_hash(args['password']).decode('utf8')
        adminDao.create(args)
        encoded_jwt = jwt.encode({"username": args["username"], "type": "admin"}, "secret", algorithm="HS256")
        return {"token": encoded_jwt.decode("utf-8")}


class AdminLoginRouter(Resource):
    def post(self):
        #a code to create default admin when it's the first time and there is no admins
        if adminDao.get_by_id(1)['username'] is None :
            args = { 'username': 'hazem', 'password': '123'}
            args['password'] = flask_bcrypt.generate_password_hash(args['password']).decode('utf8')
            adminDao.create(args)
        args = user_put_args.parse_args()
        admin = Admin.query.filter_by(username=args['username']).first()

        if not admin:
            return 'User does not exist', 404
        if flask_bcrypt.check_password_hash(admin.password, args['password']):
            encoded_jwt = jwt.encode({"username": admin.username, "type": "admin"}, "secret", algorithm="HS256")

            return {"jwt": encoded_jwt.decode('utf-8')}

        else:
            return 'wrong password!'
