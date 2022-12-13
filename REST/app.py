
# Web Framework -> Collection of Libraries to Create Websites | Creating REST APIs
# Flask - Python's Web Framework

# Package Manger - Software that installs libraries for your language of choice (pip for python)

# Flask Libaries: Request, Jsonify, Render_Template, Flask
# localhost - 127.0.0.1/ 
# port - :5000

import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# EVERY SINGLE REST API return either JSON or HTML

# Routes - Endpoint /home
@app.route('/home', methods=['GET'])
def start():
    return jsonify({'name':'Faraz'})

# Routes - Endpoint /contact
@app.route('/contact', methods=['GET'])
def contact():
    return render_template('index.html')

@app.route('/saveContact', methods=['POST'])
def saveContact():
    # Retrieve the data
    data = request.json
    print(data)
    #print(request.headers)

    # Store the data
    # Connect to a DB
    # Find what table you want to save it to
    # Save the data

    # Return success message or failure aka JSON
    return jsonify({'status':'success'})

# Starting the Flask Server on Port 4999
app.run(port=4999, debug=True)

