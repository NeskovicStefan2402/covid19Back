from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '18da407c0c7205283d9e0ecb512e3ef9'


from flaskApp import routes