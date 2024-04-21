import time
from threading import Thread

from worker import Worker

t1 = Thread(target=Worker.run_sync)
t2 = Thread(target=Worker.run_sync)
t3 = Thread(target=Worker.run_sync)

time1 = time.time()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f"Threads executed for {time.time() - time1} sec")
