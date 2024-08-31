import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4837d647660c835f577276a0d2a2e665'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
POKEMON_ID = '65935'

body_confirmation = {
    "trainer_token": TOKEN
    }

body_create = {
    "name": "PikaPika",
    "photo_id": 1
}

body_rename = {
    "pokemon_id": POKEMON_ID,
    "name": "NewPika",
    "photo_id": 2
}

body_inpokeball = {
    "pokemon_id": POKEMON_ID
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = pokemon_id = response_create.json()['id']
print(pokemon_id)

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

response_inpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_inpokeball)
print(response_inpokeball.text)