#!/usr/bin/env python2

from functools import *
from contextlib import *

#cache
@cache 
def fact(n):
    return n*fact(n-1) if n else 1
fact(10)
fact(5)
fact(12)

#cache_property

#cmp_to_key

#lru_cache
#total_ordering
@total_ordering
class Int:
    def __init__(self, x):
        self.x = x

    def __lt__(self, x):
        return self.x < x

    def __eq__(self, x):
        return self.x == x
print(Int(2) > Int(1))
print(Int(2) <= Int(1))
print(Int(2) != Int(1))

# partial - partial pre-bind args
def f1(a,b):
    print([a,b])

f1 = partial(f1, 2)
f1(4)
f1 = partial(f1, 3)
f1()
base2=partial(int, base=2)
print(base2('111'))

#partialmethod
class Cell:
    def __init__(self):
        self._alive = False
    @property
    def alive(self):
        return self._alive
    def set_state(self, state):
        self._alive = bool(state)
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)
c = Cell()
print(c.alive)
c.set_alive()
print(c.alive)


# reduce(func, seq)
nums = range(1, 100)
sum = reduce(lambda x,y: x+y, nums)
print(sum)

#singledispatch (generic func dispatched to concrete  funcs by arg/type)
@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)
fun("ok")
fun("ok", True)
fun(1, True)
## use type annotation
@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)
fun("ok", True)
fun(1, True)
fun([1,2], True)
@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)
fun([1,2], True)
fun(complex(1,2), True)
## no type annotation, pass to decorator
@fun.register(complex)
def _(arg, verbose=False):
    if verbose:
        print("Better than complicated.", end=" ")
    print(arg.real, arg.imag)
fun(complex(1,2), True)
fun(None,True)
## register pre-exists func
def nothing(arg, verbose=False):
    print("Nothing")
fun.register(type(None), nothing)
fun(None,True)
##register()return decorated func, can be stacking,pickling
from decimal import Decimal
@fun.register(float)
@fun.register(Decimal)
def fun_num(arg, verbose=False):
    if verbose:
        print("Half of your number:", end=" ")
    print(arg / 2)
fun(Decimal(100), True)
print(fun_num is fun)
## aware abc. 
from collections.abc import Mapping
fun({ 'a': 1, 'b':2}, True)
@fun.register
def _(arg: Mapping, verbose=False):
    if verbose:
        print("Key & Values")
    for key, value in arg.items():
        print(key, "=>", value)
fun({ 'a': 1, 'b':2}, True)
## check implementation chosed
print(fun.dispatch(float))
print(fun.dispatch(dict))
## access all impls
print(fun.registry.keys())
print(fun.registry[float])
print(fun.registry[object])

# singledispatchedmethod
class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg

class Negator:
    @singledispatchmethod
    @classmethod
    def neg(cls, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    @classmethod
    def _(cls, arg: int):
        return -arg

    @neg.register
    @classmethod
    def _(cls, arg: bool):
        return not arg


# update_wrapper(a, b) make a like b
def f1(x):
    print(x,x)
    pass
def g1(self):
    print('g')

print(dir(g1))
f1 = update_wrapper(f1, g1)
f1([1,2])
print(f1.__name__)
print(f1.__qualname__)
print(f1.__annotations__)
print(f1.__doc__)
print(f1.__dict__)
print(f1.__wrapped__)

# wraps = partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated).
def mydec(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('calling decorated func')
        return f(*args, **kwargs)
    return wrapper
@mydec
def example():
    ''' example docstring'''
    print("callng example")
example()
print(example.__name__)
print(example.__doc__)


