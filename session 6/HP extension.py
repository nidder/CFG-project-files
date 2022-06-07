import random
import requests

def hp_character():
    harryy = random.choice()
    url = 'http://hp-api.herokuapp.com/api/characters/'
    response= requests.get(url)
    harry = response.json()

