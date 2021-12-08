from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models.db import db
from routes.employeeRoutes import  EmployeeRouter, EmployeeListRouter
from routes.waitingRoutes import WaitingListRouter
from models.employeeModel import EmployeeModel
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sharaf:sharaf@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'secret string'
db.init_app(app)
with app.app_context():
    db.create_all()
api.add_resource(EmployeeRouter, "/employee/<int:id>")
api.add_resource(EmployeeListRouter, "/employee")
api.add_resource(WaitingListRouter, "/waiting")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
