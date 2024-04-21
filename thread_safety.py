import random
import threading
import time

l = [1, 2, 3, 4, 5, 6]

lock = threading.Lock()


def mutator():
    while True:
        lock.acquire()
        print("write")
        index = random.Random().randint(0, len(l) - 1)
        l[index] += random.Random().randint(0, 10)
        lock.release()


def reader():
    while True:
        with lock:
            print("read")
            index = random.Random().randint(0, len(l) - 1)
            if l[index] % 2 == 0:
                if l[index] % 2 != 0:
                    print("Element is odd and even!")


t1 = threading.Thread(target=mutator)
t2 = threading.Thread(target=reader)

t1.start()
t2.start()

t1.join()
t2.join()
