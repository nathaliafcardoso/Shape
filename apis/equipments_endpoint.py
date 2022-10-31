from operator import eq
from queue import Empty
from flask import request

from flask import Blueprint, jsonify, request

from apis.models.equipment import equipment

equipments_blueprint = Blueprint('equipments', __name__)

@equipments_blueprint.route('/insert_equipment', methods=['POST'])
def insert_equipment():
  assert request.path == '/insert_equipment'
  assert request.method == 'POST'

  if request.method == 'POST':
    if (request.form ['id'],request.form ['vessel_id'],request.form ['name'],request.form ['code'],request.form ['location']):
      return jsonify ({'message':'OK'}, 201)
  
  for item in equipment:
   if item is not None or Empty:
    return ({'message':'MISSING_PARAMETER'}, 400)
      
  if equipment.code is not None or Empty:
    return({'message':'REPEATED_CODE'}, 409)   

  if equipment.vessel_id is not None or Empty:
    return({'message':'NO_VESSEL'}, 409) 

  else:
    return({'message':'WRONG_FORMAT'}, 400)   

@equipments_blueprint.route('/update_equipment_status', methods=['PUT'])
def update_equipment_status():

  assert request.path == '/update_equipment_status'
  assert request.method == 'PUT'

  if request.method == 'PUT':
    if (request.form ['vessel_id'],request.form ['name'],request.form ['code'],request.form ['location']):
      return jsonify ({'message':'OK'}, 201)
  
  for item in equipment:
   if item is not None or Empty:
    return ({'message':'MISSING_PARAMETER'}, 400)
      
  if equipment.code is not None or Empty:
    return({'message':'NO_CODE'}, 409)   

  else:
    return({'message':'WRONG_FORMAT'}, 400)   
  
@equipments_blueprint.route('/active_equipments', methods=['GET'])
def active_equipment():

  assert request.path == '/active_equipments<active>'
  assert request.method == 'GET'

  if request.method == 'GET':
    if (request.form ['active'] is True):
      return jsonify (equipment.code,equipment.active,{'message':'OK'}, 201)
  
  for item in equipment:
   if item is not None or Empty:
    return ({'message':'MISSING_PARAMETER'}, 400)

  if equipment.vessel_id is not None or Empty:
    return({'message':'NO_VESSEL'}, 409) 

  else:
    return({'message':'WRONG_FORMAT'}, 400)       