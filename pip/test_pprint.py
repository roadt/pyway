

from pprint import *

class C(object):
    pass

def test(C):
    pprint(C)
    print pformat(C)
    print saferepr(C)

test(C)
test(C())
