from models import DataEntry
from peewee import fn

def get_max_energy():
    voltage_total = DataEntry.select(fn.SUM(DataEntry.voltage)).scalar() or 0

    max_energy = voltage_total / 50000
    return round(max_energy, 2)