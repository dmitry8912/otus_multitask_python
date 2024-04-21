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
        response = requests.get("https://google.com")
        return len(response.content)

    @staticmethod
    async def async_io_task(*args, **kwargs):
        response = await httpx.AsyncClient().get(url="https://google.com")
        return len(response.content)

    @staticmethod
    def cpu_task(*args, **kwargs):
        with open("for_hash.txt", "rb") as f:
            return hashlib.sha1(f.read()).hexdigest()

    @staticmethod
    def run_sync(*args, **kwargs):
        print(f"Process {os.getpid()}, Thread {threading.get_native_id()}\n")
        return Worker.cpu_task()
        # for _ in tqdm.tqdm(range(10)):
        #     time.sleep(1)
        #
        # return random.Random().randint(0, 100)

    @staticmethod
    async def run_async():
        print(f"Process {os.getpid()}, Thread {threading.get_native_id()}")
        return Worker.cpu_task()
        # for _ in tqdm.tqdm(range(10)):
        #     await asyncio.sleep(1)
        #
        # return random.Random().randint(0, 100)
