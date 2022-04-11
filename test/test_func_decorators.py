#!/usr/bin/env python2


#1
def onexit(f):
    import atexit
    atexit.register(f)
    return f

@onexit
def func():
    print 'func - called'
    pass



#2
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    pass

o1  = MyClass()
o2 = MyClass()
print id(o1) == id(o2)



#3

def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate

@attrs(versionadded="2.2",
       author