from urllib import request
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
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome') #pega o nome exato do argumento que quero aceitar
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')

        def find_hotel(hotel_id):
            for hotel in hoteis:
                if hotel['hotel_id'] == hotel_id:
                    return hotel
            return None
        
        def get(self, hotel_id):
            hotel = Hotel.find_hotel(hotel_id)
            if hotel:
                return hotel
            return {'message': 'Hotel not found'}, 404 #Status code HTTP 
        
        def post(self, hotel_id):

            dados = Hotel.argumentos.parse_args() #passo todos argumentos que foram adicionados
        
            novo_hotel = {
                'hotel_id': hotel_id,
                'nome': dados['nome'], #acessando pelas chaves - dicionario
                'estrelas': dados['estrelas'],
                'diaria': dados['diaria'],
                'cidade': dados['cidade']
         }
        
            hoteis.append(novo_hotel)
            return novo_hotel, 200 #Status Code HTTP
        
        def put(self, hotel_id):
            dados = Hotel.argumentos.parse_args() #passo todos argumentos que foram adicionados
            hotel_novo = {'hotel_id': hotel_id, **dados } #usando kwargs, posso adicionar outro argumento. é sempre restrito aos argumentos definido lá em cima
            
            hotel = Hotel.find_hotel(hotel_id)
            if hotel:
                hotel.update(hotel_novo)
                return hotel_novo, 200
            
            hoteis.append(hotel_novo)
            return hotel_novo, 201 #código HTTP criado 
        
        
        def delete(self, hotel_id):
            global hoteis
            hoteis = [hotel for hotel in hoteis if [hotel_id] != hotel_id]
            return {'message': 'Hotel deleted.'}
            pass
    