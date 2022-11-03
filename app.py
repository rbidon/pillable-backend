# imported flask package from Flask located in requirements.txt
from flask import Flask, g

# import models to be used in this application
import models
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