#!/usr/bin/env python

#
# test pickle, the persistence module dedicated to python
#
#
#
#

import sys
import os
import pickle

#
# idiot method to create a big object, which has many levels.
#
def create_big_obj(levels):
    if levels>1:
        res = []
        for n in range(levels):
            res.append(create_big_obj(levels-1))
        return res
    else:
        return range(levels)


#
# pickling and unpickling
#
#
def test_pickle():
    obj = create_big_obj(5)
    print obj

    s = pickle.dumps(obj)
    print s

    obj = pickle.loads(s)
    print obj


#
# test reference pickle,  dead loop resolution
#
class A:
    def __init__(self):
        self.b = None
        
    def __repr__(self):
        return  self.__dict__.__str__()

class B:
    def __init__(self):
        self.a = None

    def __repr__(self):
        return self.__dict__.__str__()


def test_pickle_loop():
    a = A()
    b = B()
    
    a.b = b
    b.a = a
    
    l  = [a, b]
    
    s = pickle.dumps(l)

    print pickle.loads(s)

#
#startup code
#

if __name__ == '__main__':
    test_pickle()
    test_pickle_loop()
