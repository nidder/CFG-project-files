import requests
from pprint import pprint

pokemon_number= input('Enter Pokemon ID:')
url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon_number

response =requests.get(url)
print(response)

pokemon = response.json()
print(pokemon)

pokemon_name=input
