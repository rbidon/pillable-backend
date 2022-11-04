# imported flask package from Flask located in requirements.txt
from flask import Flask, g

import os
# import dotenv to use the enivorment
from dotenv import load_dotenv

load_dotenv()  # needed to take environment variables from .env.

# import models to be used in this application
import models
# import the flask_cors to be able to use the flask in react
from flask_cors import CORS
# add the  medication models from resources
from resources.medications import medications 
DEBUG = True
PORT = os.environ.get('PORT')
# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

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

CORS(medications, origins=['http://localhost:3000'], supports_credentials=True) # so I can use it in the frontend


app.register_blueprint(medications, url_prefix='/api/v1/medications') # adding this line

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