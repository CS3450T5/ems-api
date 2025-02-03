from flask_restx import Api

from .greet import api as ns_greet


api = Api(
        title="EMS system API"
        )

api.add_namespace(ns_greet)
