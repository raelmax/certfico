from flask import render_template

from certifico import app
from certifico.forms import CertificateForm


def index():
    return render_template('index.html', form=CertificateForm(),
                           analytics=app.config.get('GOOGLE_ANALYTICS'))
