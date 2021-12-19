from flask import Flask, request
from flask_restful import Resource, reqparse, abort
import bcrypt
from dao import waitingDao, userDao
from models.waitingModel import Waiting

waiting_args = reqparse.RequestParser()
waiting_args.add_argument("id", type=int, help="my id")


class WaitingRouter(Resource):
    def get(self, id):
        result = waitingDao.get_by_id(id)
        if result["id"] == 0:
            abort(404)
        return result

    def patch(self, id):
        args = waiting_args.parse_args()
        if not waitingDao.update(args, id):
            abort(404)
        return {"data": "success"}

    def delete(self, id):
        if not waitingDao.delete(id):
            abort(404)
        return {"data": "success"}


class WaitingListRouter(Resource):
    def get(self):
        return waitingDao.get_all()

    def post(self):
        args = waiting_args.parse_args()
        waitingDao.create(args)

