import collections
from flask import Flask, jsonify, request
from flask_cors import cross_origin
import json, pymongo


app = Flask(__name__)

# GET is used for retreiving info | Arguments passed are used to assist with retreival | Ex. Search or Filters
# POST is used for saving info | Data is SECURELY sent via the body in JSON format

# Request - Used to view the requester details?
# Requests - Used to connect with an external api?

# Every flask function HAS to return JSON or XML

# CORS -> Cross Origin -> Your one service is not on the same port as the other service its calling
# CORS errors block you from doing api calls

# What is an exception? An error in executing the code. Ex. SyntaxError | TypeError
# What is validation? Writing conditions to ensure the proper outcomes of your code. 
    # Error Messaging -> Inform the user something went wrong

@app.route('/saveUser', methods=['POST'])
@cross_origin()
def saveUser():
    try:
        # Take in the data from REACT
        req = request.json
        print(req)

        # Save the Data
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['bank']             # The overall database we are connecting
        user_collection = db['user']         # The specific table we are using
        user_collection.insert_one(req)

        resp = {'msg':'success', 'error':'', 'data':'New User Was Saved!'}

    # Exception Handling
    except Exception as e:
        print(str(e))
        resp = {'msg':'fail', 'error':str(e), 'data':''}

    return jsonify(resp)


app.run(debug=True)     # Port 5000