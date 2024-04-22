import asyncio
import time

from worker import Worker


async def main():
    t1 = time.time()
    result = await asyncio.gather(Worker.run_async(), Worker.run_async(), Worker.run_async())
    print(f"Async result = {result} for {time.time() - t1} seconds")

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
