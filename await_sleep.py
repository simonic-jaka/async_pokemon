import asyncio
import time
from random import randint

start_time = time.time()


async def main():

    tasks = []

    for number in range(1, 15):
        print(f"fetching {number}")
        rnd = randint(1,2)
        tasks.append(asyncio.create_task(asyncio.sleep(rnd)))
        print(rnd, number)
    await asyncio.gather(*tasks)
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
