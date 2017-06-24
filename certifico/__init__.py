import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_sendgrid import SendGrid

app = Flask(__name__)

if os.environ.get('MONGODB_URI'):
    app.config['MONGO_URI'] = os.environ.get('MONGODB_URI')

app.config['SENDGRID_API_KEY'] = os.environ.get('SENDGRID_API_KEY')
app.config['SENDGRID_DEFAULT_FROM'] = 'contato@raelmax.com'

mail = SendGrid(app)
mongo = PyMongo(app)

import certifico.views
