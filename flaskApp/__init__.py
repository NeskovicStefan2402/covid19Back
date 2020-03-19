from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '18da407c0c7205283d9e0ecb512e3ef9'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menjacnica.db'
# db=SQLAlchemy(app)

from flaskApp import routes