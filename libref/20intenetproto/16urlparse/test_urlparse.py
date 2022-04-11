#!/usr/bin/env python2

# file:///usr/share/doc/python2/html/library/urlparse.html

# urlparse.urlpares(urlstring[,schema,[allow_fragements]])
from urlparse import urlparse


print urlparse('http://g.e-hentai.org/g/790574/c5d45b14b2/')


def file_path(self, request, response=None, info=None):
        g = request.meta['item']
        gurl = g['url']
        url = request.url
        params = gurl.split('/')[2:]
        params.append(url.split('/')[-1])
        path  =  os.path.join(*params)
        return path
