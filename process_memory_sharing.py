import time
import multiprocessing
from multiprocessing.context import Process


def print_array_contents(arr):
    while True:
        print(*arr, sep=', ')
        time.sleep(1)


if __name__ == "__main__":
    arr = multiprocessing.Array('i', [-1]*10)
    p = Process(target=print_array_contents, args=([arr]))
    p.start()

    for j in range(10):
        time.sleep(2)
        for i in range(10):
            arr[i] = j
