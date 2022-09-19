from flask_restful import Resource, reqparse

#Dicionário 
hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
        {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 390.90,
        'cidade': 'Santa Catarina'
    },
            {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'Santa Catarina'

    }
]
#primeiro recurso da api
class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis} #dicionario, na requisição vira json
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found'}, 404 #Status code HTTP 
        
    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome') #pega o nome exato do argumento que quero aceitar
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')
        
        dados = argumentos.parse_args() #passo todos argumentos que foram adicionados
        
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'], #acessando pelas chaves - dicionario
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }
        
        hoteis.append(novo_hotel)
        return novo_hotel, 200
        
    def put(self, hotel_id):
        pass
    
    def delete(self, hotel_id):
        pass
    