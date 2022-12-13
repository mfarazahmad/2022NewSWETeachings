"""
HTTP

Verbs - GET, POST - Actions on the network | What am I doing?
Endpoint - Ex. /contact | /sum | /user/add | Where am I going?

A->B
A is making a REQUEST to B
B->A
B gets the message and sends a RESPONSE

Headers - Description of the exchange | Ex. application/json
Status Codes - See the status of the exchange | 200 - Success | 400 - Client Side Error | 500 - Backend Error
Payload - Data you sent

REST is an architecture aka the how of building HTTP requests or responses+
"""

"""
Flask - Web Framework - Builds REST APIs

Libraries - jsonify() - Converts a dictionary to JSON | render_template() - Converts a HTML page to XML
Functions - run() - Starts the flask server at localhost:5000 | route() - Creates a flask endpoint
"""


from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return jsonify({
        'father':'john'
    })

@app.route('/area', methods=['GET'])
def area():
    area = .5 * 5 * 2
    return jsonify({'data':area})


app.run()

"""
class House():
    def __init__(self):
        self.year = 0
        self.price = 0
        self.color = ''


    def getYear(self):
        return self.year


farazHouse = House()
farazHouse.getYear()
kamranHouse = House()

class Flask():
    def __init__(self, fileName):
        self.fileName = fileName

    def route(endpoint, methods=['GET']):
        # Makes a flask endpoint

    def run(debug=False, port=5000):
        # Starts the flask server
"""