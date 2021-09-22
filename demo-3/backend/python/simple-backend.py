#
# Simple backend service demo
#

from flask import Flask
import socket

app = Flask(__name__)


def get_backend_signature():
    return '\n<i>Served by: ' + socket.gethostname() + '<i>\n'

def get_service(name):
    file = open('/etc/services', 'r', encoding='utf-8')
    for line in file:
        if name in line:
            yield line


@app.route('/')
def home():
    return '<html><head><title>Find service</title></head>' + \
           '<body><h2>Find service</h2>' + \
           'Usage example: http://hostname:port/service-api/find/echo' + \
           get_backend_signature() + '</body></html>\n'


@app.route('/find/<name>')
def find(name):
    result = list(get_service(name))
    response = '<html><head><title>Find service</title></head><body>\n'
    if len(result) > 0:
        response = response + '<h2>Results:</h2><ul>\n'
        for row in result:
            response = response + f'<li>{row}'
        response = response + '</ul>'
    else:
        response = response + '<b>Service not found.</b>\n'
    response = response + get_backend_signature() + '</body></html>\n'
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0")

# EOF
