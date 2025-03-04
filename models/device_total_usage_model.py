from flask_restx import fields, Model

device_total_usage_model = Model('DeviceTotal', {
    'device_id': fields.String,
    'device_total': fields.Float,
    })

