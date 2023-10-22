from threading import Thread, Lock, Condition
import time

class StingySpendy:
    money = 100
    cv = Condition() 

    def stingy(self):
        for _ in range(1000000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()
        print("Stingy done")

    def spendy(self):
        for _ in range(500000):
            self.cv.acquire()
 
            while self.money<20:
                self.cv.wait()

            self.money -= 20
            self.cv.release()
        print("Spendy done")

ss = StingySpendy()

# Create the threads and start them
thread1 = Thread(target=ss.stingy, args=()).start()
thread2 = Thread(target=ss.spendy, args=()).start()

time.sleep(5)

print(ss.money)
