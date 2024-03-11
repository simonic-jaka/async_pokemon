import requests

from utils import elapsed_timer

@elapsed_timer
def main():
    for number in range(1, 15):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(url)
        pokemon = resp.json()
        print(pokemon['name'], number)

if __name__ == "__main__":
    main()