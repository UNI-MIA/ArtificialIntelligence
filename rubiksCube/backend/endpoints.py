from flask import Blueprint, request
from flask_cors import cross_origin

from controllers import call_rubick

endpoints = Blueprint('endpoints', __name__)
@endpoints.route('/', methods=['POST', 'GET'])
def call_solver():
    try:
        if request.method == 'GET':
            return 'hola mundo'
        if request.method == 'POST':
            data = request.get_json()
            return call_rubick(data['pattern'])
    except Exception as e:
        return e
