from models import Device, DataEntry

def get_device_total_usage(device_name: str):
    voltage_total = 0
    current_total = 0
    power_total = 0
    state = ''
    count = 0
    for device in Device.select().where(Device.device_id == device_name):
        display_name = device.display_name
    for entry in DataEntry.select().join(Device).where(Device.device_id == device_name):
         voltage_total += entry.voltage
         current_total += entry.current
         power_total += entry.power
         state = entry.state
         count += 1

    return (display_name, voltage_total, current_total, power_total, state, count)
