import aiohttp
import asyncio
from asyncio import Queue

from utils import async_elapsed_timer

MAX_WORKERS = 10
MAX_REQUESTS = 50
TIME_PERIOD = 1
FETCH_SIZE = 1026


async def url_producer(max_index, max_requests, queue):
    index = 1
    run = True

    while run:
        pending = queue.qsize()
        vaccant = max_requests - pending

        tmp_index = index + vaccant
        if tmp_index >= max_index:
            tmp_index = max_index
            run = False

        for url_index in range(index, tmp_index):
            url = f"https://pokeapi.co/api/v2/pokemon/{url_index}"
            await queue.put((url, url_index))

        index = tmp_index

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

        await asyncio.create_task(url_producer(FETCH_SIZE, MAX_REQUESTS, queue))

        await queue.join()

        for task in workers:
            task.cancel()


asyncio.run(main())
