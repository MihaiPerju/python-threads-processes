import time
from multiprocessing import Process, Queue
import multiprocessing


def consumer(q):
    while True:
        txt = q.get()
        print(txt)
        time.sleep(1)


def producer(q):
    while True:
        q.put("Hello there")
        print("Message sent")
        time.sleep(1)

if __name__=="__main__":
    multiprocessing.set_start_method('spawn')  # or 'forkserver'
    queue = Queue()

    p1 = Process(target=consumer, args=[queue])
    p2 = Process(target=producer, args=[queue])

    p1.start()
    p2.start()