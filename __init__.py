from flask import Flask
from mongoengine import connect
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from flask_restful import Api
from resources.errors import errors

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://127.0.0.1:27017/demo',
    'connect': False,
}
# connect(host="mongodb://127.0.0.1:27017/demo")
# app.config['JWT_SECRET_KEY']='quanla02'

from resources.routes import initialize_routes

api = Api(app,errors=errors)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)
