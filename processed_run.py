import time
from multiprocessing import Process

from worker import Worker

if __name__ == '__main__':
    t1 = Process(target=Worker.run_sync)
    t2 = Process(target=Worker.run_sync)
    t3 = Process(target=Worker.run_sync)

    time1 = time.time()

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print(f"Processes executed for {time.time() - time1} sec")
