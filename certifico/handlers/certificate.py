from flask import request
from flask import abort
from flask import url_for
from flask import render_template

from bson.objectid import ObjectId

from certifico import mongo
from certifico import redis_queue
from certifico.mail import send_email

def create_certificate():
    logo = request.form.get('logo')
    message = request.form.get('message')
    participants = request.form.get('participants')

    if not message:
        return abort(400, 'You need provide a message to your certificate')

    if not '[participante]' in message:
        return abort(400, 'Your message need a [participante] placeholder')

    if not participants:
        return abort(400, 'You need provide a list of participants')

    participants = participants.strip().splitlines()
    participants_format = []

    for p in participants:
        try:
            person = p.split(',')
            participants_format.append({
                'name': person[0],
                'email': person[1]
            })
        except IndexError:
            pass

    if not len(participants_format):
        return abort(400, 'You provide a wrong formated participants list')

    certificate =  mongo.db.certificates.insert_one({
        'logo': logo,
        'message': message,
        'participants': participants_format
    })

    for p in participants_format:
        redis_queue.enqueue(send_email,
            to_email=p.get('email'),
            certificateLink=url_for('print_certificate', certificate=certificate.inserted_id, email=p.get('email'), _external=True)
        )

    return 'Os certificados do evento %s foram enviados.' % certificate.inserted_id

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
    message = message.replace('[participante]', participant.get('name'))

    return render_template('print.html', logo=certificate.get('logo'), message=message)
