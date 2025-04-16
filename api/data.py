from flask_restx import Namespace, Resource
from peewee import TimestampField
from datetime import datetime  # Import datetime for conversion
from functions import get_device_total_usage, get_total_usage, get_energy_source, get_max_energy, get_energy_sums
from models import device_total_usage_model, total_usage_model, max_energy_model


data_api = Namespace('data', description='Data Stats')
data_api.models[device_total_usage_model.name] = device_total_usage_model
data_api.models[total_usage_model.name] = total_usage_model
data_api.models[max_energy_model.name] = max_energy_model

@data_api.route('/total-usage/<string:start_time>/<string:end_time>')
class TotalUsage(Resource):
    def get(self, start_time, end_time):
        start_time = int(start_time)
        end_time = int(end_time)
        total = get_total_usage(start_time, end_time)
        
        return {
            'start_time': start_time,
            'end_time': end_time,
            'voltage_total': total[0],
            'current_total': total[1],
            'power_total': total[2],
        }


# max energy cap
@data_api.route('/max-energy')
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
@data_api.route('/energy-sources/<string:device_name>')
# Data = relevant data for date range
class EnergySources(Resource):
    def get(self, device_name):
        output = get_energy_source(device_name)
        return {'EnergySources': output}
    

# energy sources general read-out
# returns an array of sources with percentages of production
# in practice with our data set this returns 100% solar
@data_api.route('/energy-sources-general')
class EnergySourcesGeneral(Resource):
    def get(self):
        data = get_energy_sums()
        types = list()
        uniquetypes = list()
        for entry in data:
            if entry[0] == "facility":
                continue
            if entry[0] not in uniquetypes:
                types.append([entry[0], 0])
                uniquetypes.append(entry[0])
            for type in types:
                if entry[0] == type[0]:
                    type[1] += entry[1]
        return types


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
