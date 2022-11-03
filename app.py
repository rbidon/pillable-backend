# imported flask package from Flask located in requirements.txt
from flask import Flask, g
# import the flask_cors to be able to use the flask in react
from flask_cors import CORS

# import models to be used in this application
import models
# add the  medication models from resources
from resources.medications import medications 
DEBUG = True
PORT = 8000
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

CORS(medications, origins=['http://localhost:3000'], supports_credentials=True) # adding this line


app.register_blueprint(medications, url_prefix='/api/v1/medications') # adding this line

# default url 
@app.route('/')
def index():
    # return will display whatever is next to it 
    return 'testing routes'

# will run the app 
if __name__ == '__main__':
# invoke the method
    models.initialize()
    app.run(debug=DEBUG, port=PORT)