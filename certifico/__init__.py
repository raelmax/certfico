import os
import redis

from rq import Queue

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['SENDGRID_API_KEY'] = os.getenv('SENDGRID_API_KEY')
app.config['MONGO_URI'] = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
app.config['REDIS_URI'] = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

mongo = PyMongo(app)

redis_connection = redis.from_url(app.config.get('REDIS_URI'))
redis_queue = Queue(connection=redis_connection)

from certifico import routes
