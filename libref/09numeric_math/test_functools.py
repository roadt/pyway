
from functools import *
# High-order functions and operations on callable ojbects



# cmp_to_key(func)


# total_ordering(cls) -  fill others comparison func if class defined one of lt, le, gt, ge | eq is must   (py >=2.7)

@total_ordering
class Student:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

a = Student('Frank')
b = Student('Lisa')
a == b
a < b
a <= b
a > b 
a >= b
a != b
a <> b

# reduce(function, iterable[, initializer])  -   same as reduce,  forward compatible to py3
reduce(lambda x,y: x+y, [1,2,3])


# partial(func[, *args][, **keyword])  - return  func like partial object when called append args, keywords to origin func   -    used for partial func app with "freezes" some protion of args

basetwo = partial(int, base=2)
basetwo.__doc__ = 'convert base2 str to an int'
basetwo('10010')

r
# update_wrapper(wrapper, wrapped[,assigned][,updated])


# wraps(wrapped[, assigned][, updated])



#9.8.1 partial Object