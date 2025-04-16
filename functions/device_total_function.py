from models import Device, DataEntry
from peewee import fn

def get_device_total_usage(device_name: str):
    voltage_total = 0
    current_total = 0
    power_total = 0
    for device in Device.select().where(Device.device_id == device_name):
        display_name = device.display_name
    voltage_total = DataEntry.select(fn.SUM(DataEntry.voltage)).join(Device).where(Device.device_id == device_name).scalar()
    current_total = DataEntry.select(fn.SUM(DataEntry.current)).join(Device).where(Device.device_id == device_name).scalar()
    power_total = DataEntry.select(fn.SUM(DataEntry.power)).join(Device).where(Device.device_id == device_name).scalar()

    return (display_name, voltage_total, current_total, power_total)
