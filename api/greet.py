from flask_restx import Namespace, Resource

api = Namespace('greet', description='Greetings')


@api.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}


@api.route('/<string:name>')
class HelloPerson(Resource):
    def get(self, name):
        return {'Hello': name}
