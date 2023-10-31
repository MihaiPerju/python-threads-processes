import time
from queue import Queue
from threading import Thread

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


queue = Queue()

t1 = Thread(target=consumer, args=[queue])
t2 = Thread(target=producer, args=[queue])

t1.start()
t2.start()