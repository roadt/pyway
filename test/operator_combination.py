

class A:
    def __add__(self, b):
        print 'a.+(b)'
        return self

class B:
    def __add__(self, a):
        print 'b.+(a)'
        return self


a = A()
b = B()

a+b;
b+a;
