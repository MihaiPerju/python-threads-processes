from threading import Barrier, Thread
import time

barrier = Barrier(2)


def wait_on_the_barrier(name, time_to_sleep):
    for i in range(10):
        print(f"{name} running")
        time.sleep(time_to_sleep)
        print(f"{name} is waiting on the barrier")
        barrier.wait()

    print(f"{name} is finished")


red = Thread(target = wait_on_the_barrier, args=(["red", 4]))
blue  = Thread(target = wait_on_the_barrier, args=(["blue", 10]))

red.start()
blue.start()

time.sleep(8)
barrier.abort()