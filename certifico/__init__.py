import os
import redis

from rq import Queue

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['FROM_EMAIL'] = os.getenv('FROM_EMAIL', 'certifico@certifico.dev')
app.config['SENDGRID_TEMPLATE_ID'] = os.getenv('SENDGRID_TEMPLATE_ID')
app.config['SENDGRID_API_KEY'] = os.getenv('SENDGRID_API_KEY')
app.config['MONGO_URI'] = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
app.config['REDIS_URI'] = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
app.config['SERVER_NAME'] = os.getenv('SERVER_NAME', 'localhost:5000')
app.config['PREFERRED_URL_SCHEME'] = os.getenv('PREFERRED_URL_SCHEME', 'http')
app.config['GOOGLE_ANALYTICS'] = os.getenv('GOOGLE_ANALYTICS')

mongo = PyMongo(app)

redis_connection = redis.from_url(app.config.get('REDIS_URI'))
redis_queue = Queue(connection=redis_connection)

from certifico import routes
