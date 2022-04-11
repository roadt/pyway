

from UserDict import *


####
#  DictMixin is a mixin for object that  already defines __getitem__,__setitem__,  __delitem__, keys, mixin in all impl. other dict methods . so that you can easily build a dict-like class..   you can impl. 2 more metod  __contains__, __iter__ to boost performance..
#
# here test

class C(object):
    def __init__(self):
        self.dict  = {}
    def __getitem__(self, key):
        if self.dict.has_key(key):
            return self.dict[key]
        else:
            return None

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __delitem__(self, key):
        del self.dict[key]


    def keys(self):
        return self.dict.keys()


class CDict(DictMixin, C):
    pass

d = CDict()
print d['a']
d['a'] = 2
print d['a']
d['b'] =3

for k,v in d.iteritems():
    print k,v


print d.__class__
print dir(d.__class__)
print d.__dict__
