import aiohttp
import asyncio
from asyncio import Queue

from utils import async_elapsed_timer

MAX_WORKERS = 10
REQUESTS_PER_PERIOD = 50
TIME_PERIOD = 1
FETCH_SIZE = 1026


async def url_producer(max_index, max_requests, queue):
    index = 1
    run = True

    while run:
        pending = queue.qsize()
        vaccant = max_requests - pending

        upper_index = index + vaccant
        if upper_index >= max_index:
            upper_index = max_index
            run = False

        for pokemon_index in range(index, upper_index):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_index}"
            await queue.put((pokemon_url, pokemon_index))

        index = upper_index

        if run:
            await asyncio.sleep(TIME_PERIOD)


async def get_pokemon(session, queue):
    while True:
        url, index = await queue.get()

        async with session.get(url) as resp:
            pokemon = await resp.json()

        print(pokemon["name"], index)

        queue.task_done()


@async_elapsed_timer
async def main():

    async with aiohttp.ClientSession() as session:
        queue = Queue()

        workers = [
            asyncio.create_task(get_pokemon(session, queue)) for _ in range(MAX_WORKERS)
        ]

        await asyncio.create_task(url_producer(FETCH_SIZE, REQUESTS_PER_PERIOD, queue))

        await queue.join()

        for task in workers:
            task.cancel()


asyncio.run(main())
