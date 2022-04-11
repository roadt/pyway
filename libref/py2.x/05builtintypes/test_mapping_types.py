#!/usr/bin/env python2

# file:///usr/share/doc/python2/html/library/stdtypes.html#dict



# class dict(**kwargs)
# class dict(mapping, **kwargs)
# class dict(iterable, **kwargs)
a = dict(a=1, b=2)
b = dict(a, c=3, b=4)
c = dict(iter(b.iteritems()), d=5, a=6)
print a, b,c

# ops
# len(d)
# d[key]
# d[key] = value
# del[key]
# key in d
# key not in d
# iter(d)
# clear()
# copy()
# fromkeys(seq[, value])
# get(key[, default])
# has_key(key)
# items()
# iteritems()
# itervalues()
# keys()
# pop(key[, default])
# popitem()
# setdefault(key[, default])
# update([other])
# values()
# viewitems()
# viewkeys()
# viewvalues()

