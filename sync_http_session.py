import requests
from utils import elapsed_timer, print_ports


@elapsed_timer
def main():
    s = requests.Session()
    s.hooks["response"].append(print_ports)

    try:
        for pokemon_index in range(1, 15):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_index}"
            resp = s.get(pokemon_url)
            pokemon = resp.json()
            print(pokemon["name"], pokemon_index)
    except:
        pass
    finally:
        s.close()


if __name__ == "__main__":
    main()
