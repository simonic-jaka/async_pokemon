import requests
import time
from itertools import count

start_time = time.time()
s = requests.Session()
s.headers['Content-Type'] = ' application/vnd.api+json.'
for number in count(1):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = s.get(url, headers={'Content-Type' : 'application/vnd.api+json'})
    pokemon = resp.json()
    print(pokemon['name'], number)
s.close()
print("--- %s seconds ---" % (time.time() - start_time))