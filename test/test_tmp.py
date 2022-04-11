

def prd(o):
        for n in dir(o):
                print '------------------------%s ---------------------------' % (n)
                print getattr(o,n).__doc__




class C(object):
    
    def request?(self, r):
        if r == 1:
            return True
        else:
            return False

c = C()
print dir(c)


