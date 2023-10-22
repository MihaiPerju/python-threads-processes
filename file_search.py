import os
from os.path import isdir, join
from threading import Thread, Lock

matches = []
mutex = Lock()


def file_search(root, filename):
    print(f"Searching in: {root}")

    child_threads=[]
    for file in os.listdir(root):
        full_path = join(root, file)

        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()

        if isdir(full_path):
            t = Thread(target=file_search, args=(full_path, filename))
            t.start()
            child_threads.append(t) 

    for t in child_threads:
        t.join()

def main():
    t = Thread(target=file_search, args=(
        "/Users/michael/Desktop/python-threads-processes", "to_be_found.txt"))
    t.start()
    t.join()
    print(matches)


if __name__ == "__main__":
    main()
