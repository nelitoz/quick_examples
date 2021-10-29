# example taken from: https://likegeeks.com/downloading-files-using-python/
import requests
from clint.textui import progress

with open ("file_list.txt") as fhand:
    for url in fhand:
        url = url.strip()
        fname = url.split("/")[-1]
        r = requests.get(url, stream=True)
        with open(fname, "wb") as file:
            total_length = int(r.headers.get('content-length'))
            for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
                if ch:
                    file.write(ch)
                    