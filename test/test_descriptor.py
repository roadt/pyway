#!/usr/bin/env python2


class Dpr(object):
    def __get__(self, instance, owner):
        print [self, instance, owner]
        return [1,2,3]
    

class C(object):

    a = Dpr()

    @property
    def f(self):
        return 1

c = C()
print C.a
print c.a
print c.f()

