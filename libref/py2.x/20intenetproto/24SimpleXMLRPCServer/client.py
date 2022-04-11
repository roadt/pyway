#!/usr/bin/env python2

import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000',)
print s.pow(2,3)
print s.add(2,3)
print s.div(5,2)

#print list of available methodes
print s.system.listMethods()