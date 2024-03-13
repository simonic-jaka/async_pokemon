import aiohttp
import asyncio

from utils import async_elapsed_timer


async def get_pokemon(session, url, index):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        print(pokemon["name"], index)


@async_elapsed_timer
async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for pokemon_index in range(1, 151):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_index}"
            tasks.append(
                asyncio.create_task(get_pokemon(session, pokemon_url, pokemon_index))
            )

        await asyncio.gather(*tasks)


asyncio.run(main())
