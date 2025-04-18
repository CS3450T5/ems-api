from peewee import Model, CharField, ForeignKeyField, MySQLDatabase
from peewee import TimestampField, FloatField, IntegerField
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
