from peewee import Model, CharField, ForeignKeyField, MySQLDatabase
from peewee import TimestampField, FloatField, IntegerField

import csv
from dateutil.parser import parse

import os

database = os.environ['DB_NAME']
host = os.environ['DB_HOST']
user = os.environ['DB_USER']
passwd = os.environ['DB_PASS']


db = MySQLDatabase(database, host=host, user=user, password=passwd)


class Device(Model):
    device_id = CharField()
    display_name = CharField()
    equipment_type = CharField()

    class Meta:
        database = db


class DataEntry(Model):
    timestamp = TimestampField()
    device = ForeignKeyField(Device, backref='entries')
    voltage = FloatField(null=True)
    current = FloatField(null=True)
    power = FloatField(null=True)
    state = CharField(null=True)
    fault = IntegerField(null=True)
    entry = IntegerField()

    class Meta:
        database = db


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
