import aiohttp
import asyncio

from utils import async_elapsed_timer

@async_elapsed_timer
async def main():

    async with aiohttp.ClientSession() as session:

        for number in range(1, 15):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()

                print(pokemon['name'], number)

asyncio.run(main())
