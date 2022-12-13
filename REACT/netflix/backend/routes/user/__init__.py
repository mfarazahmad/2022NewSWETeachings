from flask import Blueprint, Flask, jsonify, request, session
from flask_cors import cross_origin
import json, os, requests, pymongo, hashlib

from scripts.InsertJson import connectToDB

userBlueprint = Blueprint('user', __name__)

@userBlueprint.route('/user/new', methods=['POST'])
@cross_origin()
def newUser():
    try:
        data = request.json
        print(data)

        #Encrypting password using sha256 algorithm
        password = hashlib.sha256(str.encode(data['password']))
        password = password.hexdigest()
        data['password'] = password

        collection = connectToDB('users')
        collection.insert_one(data)

        response = {'msg':'success', 'error': ''}
    except Exception as error:
        print(str(error))
        response = {'msg':'fail', 'error': str(error)}

    return jsonify(response)


@userBlueprint.route('/user/login', methods=['POST'])
@cross_origin()
def login():
    try:
        data = request.json
        print(data)

        username = data['username']

        collection = connectToDB('users')
        database_entry = collection.find_one({'username': username})

        # Encrypting user password entry into sha256
        password = hashlib.sha256(str.encode(data['password']))
        password = password.hexdigest()
        
        if database_entry['password'] == password:
            session['auth'] = True
            print(session)
            response = {'msg': 'success', 'error': ''}
        else:
            session['auth'] = False
            response = {'msg': 'fail', 'error': 'Wrong credentials!'}

    except Exception as e:
        print(str(e))
        response = {'msg': 'fail', 'error': str(e)}

    return jsonify(response)

@userBlueprint.route('/user/check', methods=['GET'])
@cross_origin()
def checkLogin():
    try:
        print(session)
        if 'auth' in session:
            if session['auth']:
                response = {'msg': 'success', 'error': ''}
            else:
                response = {'msg': 'fail', 'error': 'Not logged in!'}
        else:
            response = {'msg': 'fail', 'error': 'Not logged in!'}
    except Exception as e:
        print(str(e))
        response = {'msg': 'fail', 'error': str(e)}

    return jsonify(response)