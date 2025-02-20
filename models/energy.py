from peewee import Model, CharField, SqliteDatabase, ForeignKeyField, DateField, FloatField, IntegerField
import csv
db = SqliteDatabase('usage_data.db')


class Device(Model):
    device_id = CharField()
    display_name = CharField()
    equipment_type = CharField()

    class Meta:
        database = db


class DataEntry(Model):
    timestamp = DateField()
    device = ForeignKeyField(Device, backref='entries')
    voltage = FloatField(null=True)
    current = FloatField(null=True)
    power = FloatField(null=True)
    state = CharField(null=True)
    fault = IntegerField(null=True)
    entry = IntegerField()

    class Meta:
        database = db

# Very hacked together I should fix this - Zach
# Also fix my timestamp shenanagans
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
            tempDev = Device(device_id=row[0], display_name=row[1], equipment_type=row[2])
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
            entry_device = Device.select().where(Device.device_id == row[1]).get()
            tempEntry = DataEntry(timestamp=row[0], device=entry_device, voltage=row[2], current=row[3], power=row[4], state=row[6], fault=row[7], entry=row[8])
            tempEntry.save()
            print('.', end='')

if __name__ == "__main__":
    main()
