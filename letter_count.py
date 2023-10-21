import json
import urllib.request
import string
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def count_letters(url, frequency):
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1


def main():
    frequency = {}
    for c in string.ascii_lowercase:
        frequency[c] = 0

    start = time.time()

    for i in range(1000, 1020):
        count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)

    end = time.time()
    print(json.dumps(frequency, indent=4))
    print(f"Time taken: {end-start}")


main()
