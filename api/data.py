from flask_restx import Namespace, Resource

from functions import get_device_total_usage

from models import device_total_usage_model

data_api = Namespace('data', description='Data Stats')
data_api.models[device_total_usage_model.name] = device_total_usage_model


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


@data_api.route('/device-total/<string:device_name>')
class DeviceTotal(Resource):
    @data_api.marshal_with(device_total_usage_model)
    def get(self, device_name):
        totals = get_device_total_usage(device_name)
        return {'device_id': device_name,
                'device_voltage_total': totals[0],
                'device_current_total': totals[1],
                'device_power_total': totals[2],
                }
