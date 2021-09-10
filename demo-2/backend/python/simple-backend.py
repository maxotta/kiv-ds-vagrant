#
# Simple backend service demo
#

from flask import Flask

app = Flask(__name__)


def get_service(name):
    file = open('/etc/services', 'r', encoding='utf-8')
    for line in file:
        if name in line:
            yield line


@app.route('/')
def home():
    return '<html><head><title>Find service</title></head>' + \
           '<body><h2>Find service</h2>' + \
           'Usage example: http://hostname:port/service-api/find/echo</body></html>'


@app.route('/find/<name>')
def find(name):
    result = list(get_service(name))
    response = '<html><head><title>Find service</title></head><body>'
    if len(result) > 0:
        response = response + '<h2>Results:</h2><ul>'
        for row in result:
            response = response + f'<li>{row}'
        response = response + '</ul>'
    else:
        response = response + '<b>Service not found.</b>'
    response = response + '</body></html>'
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0")

# EOF
