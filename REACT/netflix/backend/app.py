import json, requests, pymongo
from flask import Blueprint, Flask, jsonify, render_template, request

from routes.movie import movieBlueprint
from routes.user import userBlueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = 'baa9c153079197ea131ce56cc01d84a76c25746fee31890f2c60e95558b6a0f2'

app.register_blueprint(movieBlueprint)
app.register_blueprint(userBlueprint)
    

app.run(debug=True)


#----- Backend Features ------

# As a User I would like for there a way to search for my Favorite Movie

# As an Engineer I would like for my movies to have a picture attached to it

# As a User I would like for my netflix session to be private (login)

# As an Engineer I'd like to setup my codebase so that the apis are seperate and scalable