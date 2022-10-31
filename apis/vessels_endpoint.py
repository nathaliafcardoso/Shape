from multiprocessing import Condition
from apis.models.equipment import equipment
from flask import Blueprint, request, jsonify
from sqlalchemy import func, extract, and_
from asyncio.windows_events import NULL
from queue import Empty

from apis.models.vessel import vessel
from apis.models.model import db

vessels_blueprint = Blueprint('vessels', __name__)

@vessels_blueprint.route('/insert_vessel', methods=['POST'])
def insert_vessel():

  assert request.path == '/insert_vessel'
  assert request.method == 'POST'

  if request.method == 'POST':
    if(request.form ['id'],request.form ['code']):
      return jsonify ({'message':'OK'}, 201)
  
  for item in vessel:
   if item is not None or Empty:
    return ({'message':'MISSING_PARAMETER'}, 400)
      
  if vessel.code is not None or Empty:
    return({'message':'FAIL'}, 409)   

  if vessel.id is not None or Empty:
    return({'message':'NO_VESSEL'}, 409) 

  else:
    return({'message':'WRONG_FORMAT'}, 400)    