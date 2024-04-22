import asyncio
import hashlib
import random
import threading
import time
import os

import httpx
import requests
import tqdm


class Worker:

    @staticmethod
    def sync_io_task(*args, **kwargs):
        for _ in range(10):
            response = requests.get("https://google.com")
        return random.Random().randint(0,100)

    @staticmethod
    async def async_io_task(*args, **kwargs):
        for _ in range(10):
            response = await httpx.AsyncClient().get(url="https://google.com")
        return random.Random().randint(0,100)

    @staticmethod
    def cpu_task(*args, **kwargs):
        for i in range(10):
            cpu_tr = 64**64**4

        return random.Random().randint(0,100)

    @staticmethod
    def run_sync(*args, **kwargs):
        print(f"Process {os.getpid()}, Thread {threading.get_native_id()}\n")
        return Worker.sync_io_task()
        # for _ in tqdm.tqdm(range(10)):
        #     time.sleep(1)
        #
        # return random.Random().randint(0, 100)

    @staticmethod
    async def run_async():
        print(f"Process {os.getpid()}, Thread {threading.get_native_id()}")
        return await Worker.async_io_task()
        # for _ in tqdm.tqdm(range(10)):
        #     await asyncio.sleep(1)
        #
        # return random.Random().randint(0, 100)
