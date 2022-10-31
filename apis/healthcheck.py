from curses import flash
from distutils.log import debug
from flask import Blueprint, jsonify, request

healthcheck_blueprint = Blueprint('healthcheck', __name__)

@healthcheck_blueprint.route('/', methods=['GET'])
def healthcheck():

 assert request.path == '/'
 assert request.method == 'GET'
 error = None

 if request.method == 'GET':
     return jsonify ({'message':'OK'}, 201)
 else:error = 'Invalid URL'