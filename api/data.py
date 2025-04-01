from flask_restx import Namespace, Resource
from peewee import TimestampField
from datetime import datetime  # Import datetime for conversion
from functions import get_device_total_usage, get_total_usage, get_max_energy
from models import device_total_usage_model, total_usage_model, max_energy_model


data_api = Namespace('data', description='Data Stats')
data_api.models[device_total_usage_model.name] = device_total_usage_model
data_api.models[total_usage_model.name] = total_usage_model
data_api.models[max_energy_model.name] = max_energy_model

@data_api.route('/total-usage/<string:start_time>/<string:end_time>')
class TotalUsage(Resource):
    def get(self, start_time, end_time):
        # Convert start_time and end_time to datetime objects
        try:
            start_time_dt = datetime.fromisoformat(start_time)
            end_time_dt = datetime.fromisoformat(end_time)
        except ValueError:
            return {"error": "Invalid datetime format. Use ISO 8601 format (e.g., 'YYYY-MM-DDTHH:MM:SS')."}, 400

        start_time = TimestampField().python_value(start_time)
        end_time = TimestampField().python_value(end_time)

        # Pass the datetime objects to get_total_usage
        total = get_total_usage(start_time_dt, end_time_dt)
        
        return {
            'start_time': start_time,
            'end_time': end_time,
            'voltage_total': total[0],
            'current_total': total[1],
            'power_total': total[2],
        }


# max energy cap
@data_api.route('max-energy/<string:date_range>')
# Data = relevant data for date range
class MaxEnergy(Resource):
    def get(self):
        max_energy = get_max_energy()
        return {'MaxEnergy': max_energy}


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
