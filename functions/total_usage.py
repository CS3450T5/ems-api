from models import Device, DataEntry
from peewee import TimestampField


def get_total_usage(start_time: TimestampField, end_time: TimestampField):
    voltage_total = 0
    current_total = 0
    power_total = 0
    for entry in DataEntry.select().join(Device).where(
        (DataEntry.timestamp >= start_time) &
        (DataEntry.timestamp <= end_time)
    ):
        voltage_total += entry.voltage
        current_total += entry.current
        power_total += entry.power


    return (voltage_total, current_total, power_total)