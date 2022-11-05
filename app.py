# imported flask package from Flask located in requirements.txt
from flask import Flask, jsonify,g

import os
# import dotenv to use the enivorment
from dotenv import load_dotenv

load_dotenv()  # needed to take environment variables from .env.
# add the  medication models from resources
from resources.medications import medications 
# add user models from resources
from resources.user import user

# import models to be used in this application
import models
# import the flask_cors to be able to use the flask in react
from flask_cors import CORS
# import the loginmanger which is neede to login & log out
from flask_login import LoginManager


DEBUG = True
PORT = os.environ.get('PORT')

app = Flask(__name__)

login_manager = LoginManager()
# Initialize an instance of the Flask class.
# This starts the website!

app.secret_key = os.environ.get('APP_SECRET')
login_manager.init_app(app)

# login_manager needed to log the user in
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

CORS(medications, origins=['http://localhost:3000'], supports_credentials=True) # so I can use it in the frontend
CORS(user, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(medications, url_prefix='/api/v1/medications')


app.register_blueprint(user, url_prefix='/users')


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response



# default url 
# @app.route('/')
# def index():
#     # return will display whatever is next to it 
#     return 'testing routes'

# will run the app 
if __name__ == '__main__':
# invoke the method
    models.initialize()
    app.run(debug=DEBUG, port=PORT)