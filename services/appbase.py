from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask_cors import CORS, cross_origin
from conf import dbconnection


global_app = Flask(__name__)
CORS(global_app)
global_app.config['SQLALCHEMY_DATABASE_URI'] = dbconnection
global_db = SQLAlchemy(global_app)
global_api = Api(global_app, version="1.0", title="Class Arrangement API", description="排课系统API")
