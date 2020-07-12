from collections import deque
from bs4 import BeautifulSoup
import urljoin
import urllib
import urllib.request

seed = "http://www.jonathanmolson.co.uk/AllAboutTheUK.html"
print ("Page to be crawled:", seed)

queue = deque([])
visited_list = []

def crawl(url):
    visited_list.append(url)
    if len(queue) > 10000:
        return

    urlf = urllib.request.urlopen(url)
    soup = BeautifulSoup(urlf.read(),features="html.parser")
    urls = soup.findAll("a", href=True)
    print(urls)

    for i in urls:
        queued = 0
        complete_url = urllib.request.urljoin(url, i["href"]).rstrip('/')

        for j in queue:
            if j == complete_url:
                queued = 1
                break

        if queued == 0:
            if len(queue) > 10000:
                return
            if (visited_list.count(complete_url)) == 0:
                queue.append(complete_url)

    current = queue.popleft()
    print("crawling ", current)
    crawl(current)

crawl(seed)

# Print queue
for i in queue:
    print (i)
print ("Pages crawled:")
# Print list of visited pages
for i in visited_list:
    print (i)