import aiohttp
import asyncio

from utils import async_elapsed_timer


async def get_pokemon(session, url, index):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return (pokemon["name"], index)


@async_elapsed_timer
async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for index in range(1, 151):
            url = f"https://pokeapi.co/api/v2/pokemon/{index}"
            tasks.append(asyncio.create_task(get_pokemon(session, url, index)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(*pokemon)


asyncio.run(main())
