import os
from os.path import isdir, join
from threading import Thread, Lock
from waitgroup import Waitgroup

matches = []
mutex = Lock()


def file_search(root, filename, wait_group):
    print(f"Searching in: {root}")

    for file in os.listdir(root):
        full_path = join(root, file)

        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()

        if isdir(full_path):
            wait_group.add(1)
            t = Thread(target=file_search, args=(full_path, filename, wait_group))
            t.start()
    
    wait_group.done()

def main():
    wait_group = Waitgroup()
    wait_group.add(1)

    t = Thread(target=file_search, args=(
        "/Users/michael/Desktop/python-threads-processes", "to_be_found.txt", wait_group))
    t.start()

    wait_group.wait()
    print(matches)


if __name__ == "__main__":
    main()
