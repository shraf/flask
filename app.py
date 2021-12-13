from flask import Flask
from flask_restful import Api, Resource
from routes.userRoutes import UserRouter, UserListRouter
from models.db import db
from routes.employeeRoutes import  EmployeeRouter, EmployeeListRouter, AttendenceRouter
from routes.waitingRoutes import WaitingListRouter
from models.employeeModel import Employee
from models.waitingModel import Waiting
from models.attendenceModel import Attendence
from flask_sqlalchemy import SQLAlchemy
import models.userModel
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sharaf:sharaf@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'secret string'
db.init_app(app)
with app.app_context():
    db.create_all()
api.add_resource(EmployeeRouter, "/employee/<int:id>")
api.add_resource(AttendenceRouter, "/employee/<int:id>/attend")
api.add_resource(EmployeeListRouter, "/employee")
api.add_resource(WaitingListRouter, "/waiting")


if __name__ == "__main__":
    app.run(debug=True)










#default code
#app = Flask(__name__)


#@app.route('/')
#def hello_world():  # put application's code here
#    return 'Hello World!'


#if __name__ == '__main__':
#    app.run()
