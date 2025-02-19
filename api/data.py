from flask_restx import Namespace, Resource

api = Namespace('data', description='Data Stats')


@api.route('/total-usage/<string:date_range>')
# Data = relevent data for date range
class TotalUsage(Resource):
    def get(self, date_range):
        return {'TotalUsage': Data}