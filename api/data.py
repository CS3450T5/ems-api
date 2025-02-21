from flask_restx import Namespace, Resource

data_api = Namespace('data', description='Data Stats')


@data_api.route('/total-usage/<string:date_range>')
# Data = relevant data for date range
class TotalUsage(Resource):
    def get(self, date_range):
        return {'TotalUsage': 'Data'}


# max energy cap
@data_api.route('max-energy/<string:date_range>')
# Data = relevant data for date range
class MaxEnergy(Resource):
    def get(self, date_range):
        return {'MaxEnergy': 'Data'}


# cost of energy production
@data_api.route('energy-cost/<string:date_range>')
# Data = relevant data for date range
class EnergyCost(Resource):
    def get(self, date_range):
        return {'EnergyCost': 'Data'}


# energy sources
@data_api.route('energy-sources/<string:date_range>')
# Data = relevant data for date range
class EnergySources(Resource):
    def get(self, date_range):
        return {'EnergySources': 'Data'}



    
