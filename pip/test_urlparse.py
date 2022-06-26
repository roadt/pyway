#!/usr/bin/env python

from  urlparse import *

url = 'http://roadt:pass@evilpowny.deviantart.com/favourites/67397771/XNA-Model-Collection?q=sdfsf&sort=desc#art-list'

# parse_qs
q=urlparse(url).query
parse_qs(q)
#parse_qsl
parse_qsl(q)
#unquote
#urldefrag
urldefrag(url)
#urljoin
#urlparse
urlparse(url)
#urlsplit
urlsplit(url)
#urlunparse
urlunparse(pr)
#urlunsplit



