import requests

from utils import elapsed_timer, print_ports


@elapsed_timer
def main():
    for pokemon_index in range(1, 15):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_index}"

        resp = requests.get(url, hooks={"response": [print_ports]})

        pokemon = resp.json()
        print(pokemon["name"], pokemon_index)


if __name__ == "__main__":
    main()
