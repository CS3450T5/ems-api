from flask import Flask
from api import api
from models import Device

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
