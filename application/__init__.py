from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_URL"]
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
db = SQLAlchemy(app)

from application import routes
from application import forms
