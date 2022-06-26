

# contextmanager
@contextmanager
def f3(x):
    print 'setup'
    try:
        yield x
    finally:
        print 'cleanup'

with f3(1) as i:
    print i

@contextmanager
def f4(l):
    print 'setup f4'
    i = iter(l)
    try:
        yield next(i)
    finally:
        print 'cleanup 4'

with f4(range(10)) as i:
        print i


#B
#
#
class F
def __enter__(self)
def _exit__(self)
d
with f(xx)

i =  f(xx)
i.__enter__
try:
    block
finally:
    i.__exit__
    

