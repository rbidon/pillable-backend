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
                               "message":f"Success ,I found {len(medications)} medications"
                               }), 200
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})
    
# CREATE(POST)
# api/v1/medications/-- will render the new data will appear
@medications.route('/', methods=['POST'])
def create_medications():
    # payload request which is the req.body of the create medications
    payload = request.get_json()
    print((payload), 'payload')
    medication =models.Medication.create(**payload)
    # medication object that will convert to model to an dict
    print(medication.__dict__)
    # see all the methods
    print(dir(medication))
    # Change the model to a dict
    medication__dict = model_to_dict(medication)
    return jsonify(data=medication__dict, status={"code": 201, "message": "Success, new medication has been added successfully"}), 200
# SHOW(GET) BY THE ID
# api/v1/medications/<id>
@medications.route('/<id>', methods=['GET'])
def get_medications_by_id(id):
    medication = models.Medication.get_by_id(id)
    print(medication) #print to see the specific medication model by id
    # if I get the correct medication return the message below
    return jsonify(
        # converting the datat into a dict to see
        data= model_to_dict(medication),
        status={
            "code":200,
            "message":f"Success, I grab the specific medication by the id"
        }
    ), 200
# UPDATE(PUT) BY THE SPECIFIC ID
# api/v1/medications/<id>
@medications.route('/<id>', methods=['PUT'])
def update_medications_by_id(id):
    payload = request.get_json()
    query = models.Medication.update(**payload).where(models.Medication.id == id)
    # grab & commit the change by query.excute()
    query.execute()
    return jsonify(
        # show the updated json data
        data = model_to_dict(models.Medication.get_by_id(id)),
        status={
            "code":200,
            "message":f"Success, I update the specific medication data by the id "
        }
    ),200

# DESTORY(DELETE) BY THE SPECIFIC ID
@medications.route('/<id>', methods=['DELETE'])
def delete_medication_by_id(id):
    query = models.Medication.delete().where(models.Medication.id == id)
    # grab & commit the change by query.excute()
    query.execute()
    return jsonify(
        data= model_to_dict(models.Medication.get_by_id(id)),
        status={
            "code":200,
            "message":f'Successfully deleted medication by id'
            }
    ), 200