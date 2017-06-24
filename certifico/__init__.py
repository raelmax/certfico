import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

if os.environ.get('MONGODB_URI'):
    app.config['MONGO_URI'] = os.environ.get('MONGODB_URI')

mongo = PyMongo(app)

import certifico.views
