import requests


pokemon_name=input('Enter pokemon ID:')
url= 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)

response =requests.get(url)
pokemon =response.json()
print(pokemon['name'])
