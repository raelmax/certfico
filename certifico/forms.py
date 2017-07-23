from flask_wtf import FlaskForm
from wtforms import HiddenField
from wtforms import FileField
from wtforms import TextAreaField

DEFAULT_CERTIFICATE_MESSAGE = '''
Certificamos que [participante] participou do CongressoABC
no dia 10 de junho na cidade de São Paulo com carga horária total de 6 horas.
'''.strip().replace('\n', ' ')

class CertificateForm(FlaskForm):
    logo_file = FileField('logo_file', id='certificate-logo')
    logo = HiddenField('logo', id='certificate-logo-value')
    message = TextAreaField('message', id='certificate-message', default=DEFAULT_CERTIFICATE_MESSAGE)
    participants = TextAreaField('participants', id='certificate-participants')
