#!/usr/bin/env python2

class C(object):
    def __init__(self, *args, **kwargs):
        super(C, self).__init__(*args, **kwargs)
        print 'C.__init__'
        pass

    def f(self):
        print 'C.f'


class M(object):
    def __init__(self, *args, **kwargs):
        super(M, self).__init__(*args, **kwargs)
        print 'M.__init__'

    def f(self):
        print 'M.f'



class N(C, M):
    def __init__(self, *args, **kwargs):
        super(N, self).__init__(*args, **kwargs)
        print 'N.__init__'

    def  f(self):
        print 'N.f'

n = N()
n.f()
print N.mro()



# so, the mixin  'overwrite' baseclass  only baseclass doens't have the method.