import time
from threading import Lock, Thread

def red_robot(lock_1, lock_2):
    while True:
        print("RED: Acquiring lock 1")
        lock_1.acquire()
        print("RED: Acquiring lock 2")
        lock_2.acquire()

        print("RED: locks acquired")
        lock_1.release()
        lock_2.release()
        print("RED: locks released")
        time.sleep(0.5)

def blue_robot(lock_1, lock_2):
    while True:
        print("BLUE: Acquiring lock 2")
        lock_2.acquire()
        print("BLUE: Acquiring lock 1")
        lock_1.acquire()

        print("BLUE: locks acquired")
        lock_1.release()
        lock_2.release()
        print("BLUE: locks released")
        time.sleep(0.5)


mutex1=Lock()
mutex2=Lock()

red = Thread(target=red_robot, args=(mutex1, mutex2))
blue = Thread(target=blue_robot, args=(mutex1, mutex2))

red.start()
blue.start()