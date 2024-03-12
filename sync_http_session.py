import requests
from utils import elapsed_timer, print_ports


@elapsed_timer
def main():
    s = requests.Session()
    s.hooks["response"].append(print_ports)

    try:
        for number in range(1, 15):
            url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            resp = s.get(url)
            pokemon = resp.json()
            print(pokemon["name"], number)
    except:
        pass
    finally:
        s.close()


if __name__ == "__main__":
    main()
