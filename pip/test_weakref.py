#!/usr/bin/env python2


import weakref

# weakref.ref(finalize_callback)
o = weakref.ref(lambda x: x)
print o, dir(o)


#weakref.mapping()
#/#m = weakref.mapping()
#print m, dir(m)

# weakref.proxy
class C(object):
    def f(self):
        pass

a = C()
wa = weakref.proxy(a)
print id(a), id(wa), wa.f()
del a
print id(wa)  
try:
    print wa.f()  # ReferenceError: weakly-referenced object no longer exists
except: 
    pass


# weakref.getweakrefcount, weakref.getweakrefs
a = C()
wa = weakref.proxy(a)
print weakref.getweakrefcount(a)
print weakref.getweakrefs(a)
print id(weakref.getweakrefs(a)[0]) == id(wa)


