from flask_pymongo import PyMongo
from app import app
import os

mongo_uri = os.getenv('mongo_uri')
app.config['MONGO_URI'] = f'{mongo_uri}'

mongo = PyMongo(app)
