from models import Device, DataEntry


def get_device_total_usage(device_name: str):
    total = 0
    for entry in DataEntry.select().join(Device).where(Device.device_id == device_name):
        total += entry.power

    return total
