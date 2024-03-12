import aiohttp
import asyncio
from asyncio import Semaphore

from utils import async_elapsed_timer

MAX_WORKERS = 5

async def get_pokemon(session, semaphore, url):
    async with semaphore, session.get(url) as resp:
        print(f"fetching {url}")

        pokemon = await resp.json()
        return pokemon['name']

@async_elapsed_timer
async def main():

    async with aiohttp.ClientSession() as session:
        semaphore: Semaphore = Semaphore(MAX_WORKERS)

        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.create_task(get_pokemon(session, semaphore, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

asyncio.run(main())
