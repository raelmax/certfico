from flask_wtf import FlaskForm
from wtforms import HiddenField
from wtforms import FileField
from wtforms import TextAreaField
from wtforms import validators

DEFAULT_CERTIFICATE_MESSAGE = '''
Certificamos que [participante] participou do CongressoABC
no dia 10 de junho na cidade de São Paulo com carga horária total de 6 horas.
'''.strip().replace('\n', ' ')

class CertificateForm(FlaskForm):
    logo_file = FileField('Logo file', id='certificate-logo')
    logo = HiddenField('Logo', id='certificate-logo-value')
    message = TextAreaField('Message', id='certificate-message',
        default=DEFAULT_CERTIFICATE_MESSAGE
    )
    participants = TextAreaField('Participants', id='certificate-participants',
        validators=[validators.required()]
    )

    def validate_message(form, field):
        if field.data == DEFAULT_CERTIFICATE_MESSAGE:
            raise validators.ValidationError('You need provide a custom text to your form message')
        elif not '[participante]' in field.data:
            raise validators.ValidationError('Your message need a [participante] placeholder')

    def validate_participants(form, field):
        # please, refactor me :(
        data = field.data.strip().splitlines()
        cleared_data = []

        for participant in data:
            try:
                person = participant.split(',')
                cleared_data.append({'name': person[0], 'email': person[1]})
            except IndexError:
                pass

        if not len(cleared_data):
            raise validators.ValidationError('You provide a wrong formated participants list')

        form.participants_list = cleared_data
