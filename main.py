from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models.db import db
from routes.userRoutes import  UserRouter, UserListRouter
from models.userModel import UserModel
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sharaf:sharaf@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'secret string'
db.init_app(app)
with app.app_context():
    db.create_all()
api.add_resource(UserRouter, "/user/<int:id>")
api.add_resource(UserListRouter, "/user")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
