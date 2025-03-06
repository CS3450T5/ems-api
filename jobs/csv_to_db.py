from models import db, Device, DataEntry
import csv
from dateutil.parser import parse


def main():
    db.connect()
    db.create_tables([Device, DataEntry])
    with open('devices.csv', newline='') as devices:
        reader = csv.reader(devices)
        for row in reader:
            # ID = 0
            # display name = 1
            # equpment type = 2
            # ip = 3
            print(f"ID: {row[0]}")
            print(f"Display Name: {row[1]}")
            print(f"Equp. Type = {row[2]}")
            tempDev = Device(device_id=row[0],
                             display_name=row[1],
                             equipment_type=row[2])
            tempDev.save()

    with open('entries.csv', newline='') as entries:
        reader = csv.reader(entries)
        for row in reader:
            # timestamp = 0
            # device = 1
            # voltage = 2
            # current = 3
            # power = 4
            # state = 6
            # fault = 7
            # entry = 8
            entry_device = Device.get(Device.device_id == row[1])
            tempEntry = DataEntry(timestamp=int(parse(row[0]).strftime('%s')),
                                  device=entry_device,
                                  voltage=row[2],
                                  current=row[3],
                                  power=row[4],
                                  state=row[6],
                                  fault=row[7],
                                  entry=row[8])
            tempEntry.save()


if __name__ == "__main__":
    main()
