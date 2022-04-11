#!/usr/bin/python3

print('hello')

from urllib import request

x = request.urlopen('http://m.baidu.com')
print(x.read())