import flask_bcrypt
from flask import Flask, request
from flask_restful import Resource, reqparse, abort
from dao import adminDao
from models.adminModel import Admin
from flask_restful import inputs
from flask_bcrypt import Bcrypt

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("id", type=int, help="id")
user_put_args.add_argument("username", type=str, help="username")
user_put_args.add_argument("password", type=str, help="password")
class AdminRegisterRouter(Resource):
    def get(self):
        return adminDao.getAll()
    def post(self):
        args = user_put_args.parse_args()
        args['password']=flask_bcrypt.generate_password_hash(args['password']).decode('utf8')
        adminDao.create(args)

class AdminLoginRouter(Resource):
    def post(self):
        args = user_put_args.parse_args()
        admin=Admin.query.filter_by(username=args['username']).first()
        if not admin:
            return 'User does not exist', 404
        if flask_bcrypt.check_password_hash(admin.password , args['password']):
            return f'Welcome back {admin.username}'
        else:
            return 'wrong password!'
