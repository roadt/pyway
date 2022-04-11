#!/usr/bin/env python2

class C:
    def f(cls, arg1, arg2):
        print [cls, arg1, arg2]
    f = classmethod(f)

    def g(self):
        pass

C.f(1, 2)
print type(C.f)   ' instacemethod'
print type(C.g) ' instancemethod'


def h():
    pass
print type(h)   'instancemethod'
h = classmethod(h)
print type(h)  # -> 'classmethod'
        
