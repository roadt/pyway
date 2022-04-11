#!/usr/bin/env python2


class C:
    i = 1

    def f(self):
        pass

c = C()
assert c.i == 1
c.i = 2
assert C.i == 1
assert c.i == 2

c.j = 3
assert c.j == 3
# result:  var in classdef is class var. only chagen by C.i.   c.i inherit value of C.i, and put change back to c.i.



    

    
    