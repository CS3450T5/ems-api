from models import Device, DataEntry

def get_max_energy():
    # Initialize the total voltage
    voltage_total = 0

    # Iterate through all devices and sum their voltage
    for entry in DataEntry.select(DataEntry.voltage).join(Device):
        voltage_total += entry.voltage

    # Divide the total voltage by 50,000
    result = voltage_total / 50000

    # Return the result
    return result
