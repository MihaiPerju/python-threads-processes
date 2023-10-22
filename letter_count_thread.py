import json
import urllib.request
import string
import time
from threading import Thread, Lock

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

finished_count = 0



def count_letters(url, frequency, mutex):
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    txt = str(response.read())
    mutex.acquire()

    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    
    global finished_count
    finished_count += 1
    mutex.release()



def main():
    frequency = {}
    mutex = Lock()
    for c in string.ascii_lowercase:
        frequency[c] = 0

    start = time.time() 

    for i in range(1000, 1020):
        Thread(target=count_letters, args=(
            f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()


    while True:
        mutex.acquire()
        if finished_count==20:
            break
        mutex.release()
        
        time.sleep(0.5)

    end = time.time()
    print(json.dumps(frequency, indent=4))
    print(f"Time taken: {end-start}")


main()
