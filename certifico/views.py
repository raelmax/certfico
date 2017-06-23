from flask import request
from flask import abort
from flask import render_template

from bson.objectid import ObjectId

from certifico import app
from certifico import mongo

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send-certificates', methods=['POST'])
def create():
    logo = request.form.get('logo')
    message = request.form.get('message')
    participants = request.form.get('participants', '')
    participants = [{'name': p.split(',')[0], 'email': p.split(',')[1]} for p in participants.strip().splitlines()]

    certificate =  mongo.db.certificates.insert({
        'logo': logo,
        'message': message,
        'participants': participants
    })
    return 'Os certificados do evento %s foram enviados.' % certificate

@app.route('/print/<certificate>/', methods=['GET'])
def print(certificate):
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
