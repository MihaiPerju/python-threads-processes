from threading import Thread, Lock
import time

class StingySpendy:
    money = 100
    mutex = Lock() 

    def stingy(self):
        for _ in range(1000000):
            self.mutex.acquire()
            self.money += 0.5
            self.mutex.release()
        print("Stingy done")

    def spendy(self):
        for _ in range(1000000):
            self.mutex.acquire()
            self.money -= 0.5
            self.mutex.release()
        print("Spendy done")

ss = StingySpendy()

# Create the threads and start them
thread1 = Thread(target=ss.stingy, args=()).start()
thread2 = Thread(target=ss.spendy, args=()).start()

time.sleep(5)

print(ss.money)
