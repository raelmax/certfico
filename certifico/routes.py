from certifico import app
from certifico import handlers

app.add_url_rule('/',
                 view_func=handlers.index, methods=['GET'])
app.add_url_rule('/send-certificates',
                 view_func=handlers.create_certificate, methods=['POST'])
app.add_url_rule('/print/<certificate>/',
                 view_func=handlers.print_certificate, methods=['GET'])
