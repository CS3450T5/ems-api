from flask import Flask
from flask_cors import CORS  # Import CORS
from api import api
import os

#debug = os.environ['DEBUG']

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire application
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
