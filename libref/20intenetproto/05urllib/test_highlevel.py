


import urllib
from six import print_

#urllib.urlopen(url[, data[, proxies[, context]]])¶
urllib.urlopen('http://xx.aaaaaa')   # IOError - socket error - name/service not known
urllib.urlopen('http://192.168.22.22')  # IOError - can't connt
file = urllib.urlopen('http://news.163.com')
file.readline()
file.read()
file.fileno()
file.info()
file.info().items()
file.getcode()
file.geturl()
file.close()
urllib.urlopen('http://www.baidu.com/s?wd=ff').read()




#urllib.urlretrieve(url[, filename[, reporthook[, data]]])¶
def report(*args, **kwargs):
    print_(args, kwargs)
file =  urllib.urlretrieve('http://news.163.com', 'new163.html', report)


#urllib._urlopener
class UAURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
urllib._urlopener = UAURLopener()
urllib.urlopen('http://www.baidu.com').read()

#urllib.urlcleanup()
urllib.urlcleanup()




##  utilty functions

#urllib.quote(string[,safe])
urllib.quote("我们")
urllib.quote('/<a>/[b]/(c)/&|^/')
urllib.quote('/<a>/[b]/(c)/&|^/', '/()<>[]')
urllib.quote("a b")

#urllib.quote_plus(string[,safe])
urllib.quote_plus("我们")
urllib.quote_plus('/<a>/[b]/(c)/&|^/')   # / is escaped.
urllib.quote_plus('/<a>/[b]/(c)/&|^/', '/()<>[]')
urllib.quote_plus("a b")  #  space is quoted to '+'


#urllib.unquote(string)
urllib.unquote(urllib.quote('/<a>/[b]/(c)/&|^/'))
urllib.unquote('a+b')   #  + is still + 

#urllib.unquote_plus(string)
urllib.unquote_plus('a+b')


#urllib.urlencode(query[, doseq])¶
urllib.urlencode({'a': 1, 'b':2})
urllib.urlencode([('a', 1), ('b', 2)])
urllib.urlopen

#urllib.pathname2url(path)

#urllib.url2pathname(path)

#urllib.getproxies()
urllib.getproxies()