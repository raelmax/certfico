from flask import request
from flask import abort
from flask import url_for
from flask import render_template

from bson.objectid import ObjectId

from certifico import app
from certifico import mongo
from certifico import redis_queue
from certifico.mail import send_email
from certifico.forms import CertificateForm

def create_certificate():
    form = CertificateForm()

    if form.validate_on_submit():
        certificate =  mongo.db.certificates.insert_one({
            'logo': form.data['logo'],
            'message': form.data['message'],
            'participants': form.participants_list
        })

        for p in form.participants_list:
            redis_queue.enqueue(send_email,
                to_email=p.get('email'),
                certificateLink=url_for('print_certificate', certificate=certificate.inserted_id, email=p.get('email'), _external=True)
            )

        return 'Os certificados do evento %s foram enviados.' % certificate.inserted_id
    return render_template('index.html', form=form,
                           analytics=app.config.get('GOOGLE_ANALYTICS')), 400

def print_certificate(certificate):
    email = request.args.get('email')

    if not email:
        return abort(404)

    certificate = mongo.db.certificates.find_one_or_404({'_id': ObjectId(certificate)})

    try:
        participant = next(filter(lambda p: p.get('email') == email, certificate.get('participants')))
    except StopIteration:
        return abort(404)

    message = certificate.get('message')
    message = message.replace('[participante]', participant.get('name').upper())

    return render_template('print.html', logo=certificate.get('logo'), message=message)
