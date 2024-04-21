import concurrent.futures
import time
from concurrent.futures import ThreadPoolExecutor

from worker import Worker

with ThreadPoolExecutor() as executor:
    time1 = time.time()
    results = executor.map(Worker.run_sync, [1, 2, 3])

    for i in results:
        print(f"Result from thread={i}")

print(f"Threads executed for {time.time() - time1} sec")
