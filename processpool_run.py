import concurrent.futures
import time
from concurrent.futures import ProcessPoolExecutor

from worker import Worker

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        time1 = time.time()
        results = executor.map(Worker.run_sync, [1, 2, 3])

        for i in results:
            print(f"Result from process={i}")

    print(f"Threads executed for {time.time() - time1} sec")