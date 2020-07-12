import requests
from html.parser import HTMLParser

seed = "http://www.jonathanmolson.co.uk/AllAboutTheUK.html"
frontier = []
count = 0

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        global count
        if tag ==  "a":
            for attr in attrs:
                if attr[0] == 'href':
                    if attr[1].find("http") >= 0:
                        frontier.append(attr[1])
                
x=0
while x == x:
    parser = MyHTMLParser()
    r = requests.get(seed)
    parser.feed(r.text)
    seed = frontier[x]
    print(frontier)
    x += 1

    

print(frontier)