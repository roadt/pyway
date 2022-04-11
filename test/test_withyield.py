
import contextlib


#1
class C(object):
    def __init__(self,r):
        self.r = r
    def __enter__(self):
        print 'start',self.r
    def __exit__(self, type, value, traceback):
        print 'stop', self.r
with C(1):
    print 2


# 2 --
print '----------'
@contextlib.contextmanager
def f(r):
    print "start", r
    try:
        yield
    finally:
        print "stop", r

with  f(1):
    print 2
