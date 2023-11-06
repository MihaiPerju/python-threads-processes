package main

import (
	"fmt"
	"sync"
	"time"
)

func redRobot(lock1, lock2 *sync.Mutex) {
	for {
		fmt.Println("RED: Acquiring lock 1")
		lock1.Lock()
		fmt.Println("RED: Acquiring lock 2")
		lock2.Lock()

		fmt.Println("RED: locks acquired")
		lock1.Unlock()
		lock2.Unlock()
		fmt.Println("RED: locks released")
		time.Sleep(500 * time.Millisecond)
	}
}

func blueRobot(lock1, lock2 *sync.Mutex) {
	for {
		fmt.Println("BLUE: Acquiring lock 2")
		lock2.Lock()
		fmt.Println("BLUE: Acquiring lock 1")
		lock1.Lock()

		fmt.Println("BLUE: locks acquired")
		lock1.Unlock()
		lock2.Unlock()
		fmt.Println("BLUE: locks released")
		time.Sleep(500 * time.Millisecond)
	}
}

func main() {
	mutex1 := &sync.Mutex{}
	mutex2 := &sync.Mutex{}

	go redRobot(mutex1, mutex2)
	go blueRobot(mutex1, mutex2)

	select {}  // This will keep main from exiting
}
