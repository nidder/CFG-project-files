import random
import requests

def random_pokemon():
    pokemon_number = random.randint(1,151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return{
    'name': pokemon['name'],
    'height': pokemon['height'],
    'id':  pokemon['id'],
    'weight': pokemon['weight'],
    'moves_number': len(pokemon['moves'])
    }

print('moves {}'.format(random_pokemon()))



















