import bcrypt
from flask import Flask
from flask_restful import Api, Resource
from routes.userRoutes import UserRouter, UserListRouter
from models.db import db
from routes.employeeRoutes import  EmployeeRouter, EmployeeListRouter, AttendenceRouter,EmployeeLoginRouter
from routes.adminRoutes import AdminRegisterRouter,AdminLoginRouter
from routes.waitingRoutes import WaitingListRouter
from models.employeeModel import Employee
from models.waitingModel import Waiting
from models.attendenceModel import Attendence
from flask_sqlalchemy import SQLAlchemy
import models.userModel
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt=Bcrypt(app)

api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hazem@localhost/attendance'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'secret string'
db.init_app(app)
with app.app_context():
    db.create_all()
api.add_resource(EmployeeRouter, "/employee/<int:id>")
api.add_resource(AttendenceRouter, "/employee/<int:id>/attend")
api.add_resource(EmployeeListRouter, "/employee")
api.add_resource(WaitingListRouter, "/waiting")
api.add_resource(AdminRegisterRouter,"/adminregister")
api.add_resource(AdminLoginRouter,"/adminlogin")
api.add_resource(EmployeeLoginRouter,"/employeelogin")
if __name__ == "__main__":
    app.run(debug=True)










#default code
#app = Flask(__name__)


#@app.route('/')
#def hello_world():  # put application's code here
#    return 'Hello World!'


#if __name__ == '__main__':
#    app.run()
