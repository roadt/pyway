import requests
from htmlparsing import Element
url = 'https://python.org/'
r = requests.get(url)

e = Element(text=r.text)

import pprint
pprint.pprint([e.links,
e.absolute_links,
e.xpath('//a')[0].attrs,
e.xpath('//a')[0].attrs.title,
e.css('a')[0].attrs,
e.parse('<a href="#content" title="Skip to content">{}</a>'),
e.css('a')[5].text,
e.css('a')[5].html,
e.css('a')[5].markdown])
