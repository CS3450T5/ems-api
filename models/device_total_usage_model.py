from flask_restx import fields, Model

device_total_usage_model = Model('DeviceTotal', {
    'device_id': fields.String,
    'device_voltage_total': fields.Float,
    'device_current_total': fields.Float,
    'device_power_total': fields.Float,
    })

