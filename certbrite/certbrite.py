from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    certificate_text = request.form.get('certificate-text', '')
    certificate_theme = request.form.get('certificate-theme', 'theme-1')
    return render_template('preview.html', text=certificate_text,
                                           theme=certificate_theme)
