import threading
import time
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]


def fetch_content(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
# for url in urls:
#     fetch_content(url)---- to fetch this 3 urls it took about 5 seconds 


# now with threading
threads = []
#starting threading
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

#waiting for thread to finish
for thread in threads:
    thread.join()
### with threading it took about 1.72 seconds only
end_time = time.time() - start_time
print("finished:",end_time)