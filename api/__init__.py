from flask_restx import Api

from .greet import greet_api as ns_greet
from .data import data_api as ns_data


api = Api(
        title="EMS system API"
        )

api.add_namespace(ns_greet)
api.add_namespace(ns_data)
