from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '69be2065580be7fda82ac52f294ba94f'
#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/test'
db = SQLAlchemy(app)

from flask_proj import routes
