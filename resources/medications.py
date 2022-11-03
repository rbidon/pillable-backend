# import models to be uses in this medication controller/routes
import models

# import the Blueprint 
from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

# create Blueprint to be used in this medication controller
# first arg - blueprint name
# second arg = import name 
medications = Blueprint('medications', 'medications')

# added the router to this 
# INDEX ROUTE(GET)
# api/v1/medications/
@medications.route('/', methods=['GET'])
def medications_index():
    try: 
        medications =[model_to_dict(medication) for medication in models.Medication.select()]
        # medications_dict = []
        # for medication in result:
        #     medication_dict = model_to_dict(dog)
        #     medications_dict.append(dog_dict)
        print(medications)
        return jsonify(data=medications, 
                       status={"code":200,
                               "message":"Success"
                               })
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})
    
# CREATE(POST)
# api/v1/medications/-- will render the new data will appear
@medications.route('/', methods=['POST'])
def create_medications():
    # payload request which is the req.body of the create medications
    payload = request.get_json()
    print(type(payload), 'payload')
    medication =models.Medication.create(**payload)
    # medication object that will convert to model to an dict
    print(medication.__dict__)
    # see all the methods
    print(dir(medication))
    # Change the model to a dict
    medication__dict = model_to_dict(medication)
    return jsonify(data=medication__dict, status={"code": 201, "message": "Success, new medication has been added successfully"})
# UPDATE(PUT)
# DESTORY(DELETE)