from flask_restx import Namespace, Resource
from models import Device, db, DataEntry

api = Namespace('greet', description='Greetings')


@api.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}


@api.route('/<string:name>')
class HelloPerson(Resource):
    def get(self, name):
        return {'Hello': name}

      
@api.route('/test')
class TestDb(Resource):
    def get(self):
        # Would be better to have a set of files just for retrieval
        # so then you don't have to deal with peewee stuff but for now
        # this is good enough just to have it here
        db.connect()
        test = Device.select()
        return {'test': test[1].device_id}