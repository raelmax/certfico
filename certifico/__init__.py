import os

from rq import Queue

from flask import Flask
from flask_pymongo import PyMongo

from certifico.worker import conn

app = Flask(__name__)

if os.environ.get('MONGODB_URI'):
    app.config['MONGO_URI'] = os.environ.get('MONGODB_URI')

app.config['SENDGRID_API_KEY'] = os.getenv('SENDGRID_API_KEY')

mongo = PyMongo(app)
redis_queue = Queue(connection=conn)

import certifico.views
