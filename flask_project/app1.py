from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    players = []

    def get(self):
        return {"players_s": self.players}

    def post(self):
        self.players.append("san")
        return {"msg": "player added"}

api.add_resource(HelloWorld, '/Resource')  

if __name__ == '__main__':
    app.run(debug=True)
