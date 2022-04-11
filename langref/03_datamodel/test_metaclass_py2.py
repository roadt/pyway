#!/usr/bin/env python2


class metacls(type):
    def __new__(mcs, name, bases, dict):
        dict['foo'] = 'metacls was here'
        return type.__new__(mcs, name, bases, dict)

class C:
    __metaclass__ = metacls

c = C()
print c.foo
