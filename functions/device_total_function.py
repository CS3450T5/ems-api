from models import Device, DataEntry


def get_device_total_usage(device_name: str):
    voltage_total = 0
    current_total = 0
    power_total = 0
    for entry in DataEntry.select().join(Device).where(Device.device_id == device_name):
        voltage_total += entry.voltage
        current_total += entry.current
        power_total += entry.power


    return (voltage_total, current_total, power_total)
