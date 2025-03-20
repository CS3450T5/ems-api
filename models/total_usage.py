from flask_restx import fields, Model

total_usage_model = Model('TotalUsage', {
    'start_time': fields.DateTime,
    'end_time': fields.DateTime,
    'voltage_total': fields.Float,
    'current_total': fields.Float,
    'power_total': fields.Float,
    })

