from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random
#importing our own self-made API
from model.pokemons import *

pokemon_api =  Blueprint('pokemon_api', __name__,
                   url_prefix='/api/pokemons')

#Defining our api as the pokemon API
api = Api(pokemon_api)

#Defining Pokemon Class
class PokemonsAPI:
    
    class _Create(Resource):
        def post(self, pokemon):
            pass
# Defining functinos to Read the pokemon information, reads information for all the classes and definations
    class _Read(Resource):
        def get(self):
            return jsonify(getPokemons())
        
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getPokemon(id))
    
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomPokemon())
        
    class _ReadCount(Resource):
        def get(self):
            count = countPokemons()
            countMsg = {'count': count}
            return jsonify(countMsg)
    
# Updating Upvotes on the side and making take effect
    class _UpdateUpVote(Resource):
        def put(self, id):
            addUpVote(id)
            return jsonify(getPokemon(id))
#Updating Downvotes on the site and making it actually take effect
    class _UpdateDownVote(Resource):
        def put(self, id):
            addDownVote(id)
            return jsonify(getPokemon(id))  
        
# Defining URLS for all of the api subpages
    api.add_resource(_Create, '/create/<string:pokemon>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateUpVote, '/upvote/<int:id>')
    api.add_resource(_UpdateDownVote, '/downvote/<int:id>') 
    
# Server URL stuff to create actual pathway to site
if __name__ == "__main__": 
    
    server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/pokemons"
    responses = [] 
    
    #adding code to make sure the upvotes, downvotes and get information run and work properly
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']
    
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read pokemon by id
        ) 
    responses.append(
        requests.put(url+"/upvote/"+num) # add to upvote count
        ) 
    responses.append(
        requests.put(url+"/downvote/"+num) # add to downvote count
        ) 
    
    responses.append(
        requests.get(url+"/random")  # read a random pokemon
        ) 
    
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")