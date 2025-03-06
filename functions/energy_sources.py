from models import Device, DataEntry

# returning the type of energy source for a given device
# i'm thinking that you'd call this function for each device maybe in conjunction with
# the device_total_function to group the sources?
# but it depends. shrug emoji
def get_energy_source(device_name: str):
    for device in Device.select().where(Device.device_id == device_name):
        return device.equipment_type

# also note that some devices don't have equipment types for some reason.
# and that some of the devices are unclear about types ("facility" or "meter")
# this will require a bit of additional work later to clarify the sources. 
# also some of the devices are "in" and some are "out"
# like "charger" vs "solar"
# anyways TLDR for now just returning equipment type but this will need some changes later.
