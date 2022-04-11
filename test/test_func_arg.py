

def pr(o):
    for n in dir(o):
        print n, ' -> ' ,getattr(o,n)




def f(i=1,j=2,*a,**kw):
    print i,j,a,kw

f(2,1,3,4,a=1)
f(i=2,a=3)


def f2(r,*a,**kw):
    print r,a,kw

f2(1,i=1,j=2)
f2(*[1,2],**{'i':1,'j':2})

def f3(i,j):
    print i,j

f3(*[],**{'i':1,'j':2})



def f4(i,j,*a,**kw):
    pass

pr(f4.func_code)




#=============

def f5(i,j,*a,**kw):
    print i,j,a,kw

f5(1,2)
#f5 (1,2,i=3)       #TypeError: f5() got multiple values for keyword argument 'i'
f5(1,j=3,*(1,2),{'i':1})    # SyntaxError: non-keyword arg after keyword arg

