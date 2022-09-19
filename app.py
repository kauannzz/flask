from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app) #API instanciada, gerencia tudo.

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')


if __name__== '__main__':
    app.run(debug=True) #somente quando estamos produzindo