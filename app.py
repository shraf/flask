import flask_bcrypt
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from routes.userRoutes import UserRouter, UserListRouter
from models.db import db
from routes.employeeRoutes import  EmployeeRouter, EmployeeListRouter, AttendanceRouter,EmployeeLoginRouter,exist
from routes.adminRoutes import AdminRegisterRouter,AdminLoginRouter
from routes.waitingRoutes import WaitingListRouter
from models.employeeModel import Employee
from models.waitingModel import Waiting
from models.attendenceModel import Attendance
from flask_sqlalchemy import SQLAlchemy
import models.userModel
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt=Bcrypt(app)


api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ptakwcnqewexqw:884d2268ed8bdb29c9250e13eff717d31e2bc0770c3ed2b2b4fd140f60bb946d@ec2-184-73-25-2.compute-1.amazonaws.com:5432/d6h95qrj7stcno'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'secret string'
db.init_app(app)
with app.app_context():
    db.create_all()



api.add_resource(EmployeeRouter, "/employee/<int:id>")
api.add_resource(AttendanceRouter, "/employee/<int:id>/attend")
api.add_resource(EmployeeListRouter, "/employee")
api.add_resource(WaitingListRouter, "/waiting")
api.add_resource(AdminRegisterRouter,"/admin/register")
api.add_resource(AdminLoginRouter,"/admin/login")
api.add_resource(EmployeeLoginRouter,"/employee/login")
api.add_resource(exist,"/employee/exist/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)








