import requests
from htmlparsing import Element, HTMLParsing, Text, Attr, Parse

url = 'https://news.ycombinator.com/item?id=16476454'
r = requests.get(url)
article_detail = HTMLParsing(r.text).detail({'title': Text('.titleline a'),
                                             'points': Parse('span.score', '>{} points'),
                                             'link': Attr('.titleline a', 'href')})
print(article_detail)
