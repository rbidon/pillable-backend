# handle the controller for login/logout/register
import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

# Create Blueprint to be used in this user controller 
user= Blueprint('users','user',url_prefix='/user')
# all api will be /api/v1/user/register

@user.route('/register', methods=['POST'])
def register():
    payload = request.get_json()
    # accept the email model to be in lowercase 
    payload['email'] = payload['email'].lower
    # will use the email to register into the account
    try:
        models.User.get(models.User.email == payload['email'])
        # if you have the email in the db already you can nofity me if not
        return jsonify(
            date={},
            status={
                "code": 401,
                "message": "This user email already exist so you don't need to register instead log in"}
        )
        # if the email doesn't exist create a user account model
    except:
    # payload password = secure the password so you dont see it
        payload['password'] = generate_password_hash(payload['password'])
        user= models.User.create(**payload)
        
        # start the user session
        login_user(user)
        
        user_dict = model_to_dict(user)
        print(user_dict)
        print(type(user_dict))
        # delete the passwaord before we return it
        del user_dict['password']
        return jsonify(data=user_dict, status={"code": 201, "message": "Success new user has register to the account"}), 201
