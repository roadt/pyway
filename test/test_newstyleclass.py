#!/usr/bin/env python


import sys
import os


class Meta(type):
    def __getattribute__(*args):
        print "Metaclass.__getattribute__"
        return object.__getattribute__(*args)

class A:
    def __init__(self):
        self.i = 1
        
    def __getstate__(self):
        return [2]

class B(object):
    def __init__(self):
        self.j = 1

    def __getattribute__(self, name):
        if name.startswith('__'):
            return  object.__getattribute__(self, name)
        else:
            raise AttributeError('not a')

    def __getattr__(self, name):
        return 'value of %s from __getattr__' % name


class C:
    __metaclass__ = Meta
    __slots__ = [ 'a', 'b' ]
    def __init__(self):
        self.a = 1
        self.b = 2

    def __len__(self):
        return  C.__slots__.__len__()

    def __getitem__(self, n):
        return self.__getattribute__(n)

    def __contains__(self, item):
        print self, item
        return item in C.__slots__

    def __iter__(self):
        for n in C.__slots__:
            yield self.__getattribute__(n)

    def __reversed__(self):
        for n in reversed(C.__slots__):
            yield self.__getattribute__(n)


    def __getattribute__(self, name):
        print '__getattribute__ %s' % name
        if name.startswith('__'):

            return  object.__getattribute__(self, name)
        else:
            raise AttributeError('not a')

    def __getattr__(self, name):
        return 'value of %s from __getattr__' % name

#
# for pickle , unpickle
#
    def __getstate__(self):
        return 1
        

class D(object):
    def __init__(self):
        self.a = 1
        self.b = 2

#    def __getstate__(self):
#       return [3]


class MUnpickler(pickle.Unpickler):
    def load_global(*args):
        print args
        pickel.Unpickler.load_global(*args)


print 'loaded'



