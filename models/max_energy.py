from flask_restx import fields, Model

max_energy_model = Model('MaxEnergy', {
    'max_energy': fields.Float,
    })