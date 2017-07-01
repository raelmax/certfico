from flask import render_template

from certifico import app

def index():
    return render_template('index.html', analytics=app.config.get('GOOGLE_ANALYTICS'))
