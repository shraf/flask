from flask import Flask, request
from flask_restful import Resource, reqparse, abort

from dao import waitingDao
from models.waitingModel import WaitingModel

waiting_args = reqparse.RequestParser()
waiting_args.add_argument("id", type=int, help="my naaame")

class WaitingRouter (Resource):
    def get(self, id):
        result = waitingDao.getById(id)
        if(result["id"]==0):
            abort(404)
        return result
    def patch(self, id):
        args = waiting_args.parse_args()
        if(waitingDao.update(args,id)==False):
            abort(404)
        return {"data":"success"}

    def delete(self, id):
        if(waitingDao.delete(id)==False):
            abort(404)
        return {"data":"success"}
class WaitingListRouter(Resource):
    def get(self):
        return waitingDao.getAll()
    def post(self):
        args = waiting_args.parse_args()
        waitingDao.create(args)