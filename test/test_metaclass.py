

class TestMeta(type):
    def __new__(mcs, class_name, bases, attrs):
        print [mcs, class_name, bases, attrs]
        cls = type.__new__(mcs, class_name, bases, attrs)
        cls.f = 1
        return cls

class C(object):
    __metaclass__ = TestMeta


c  = C()
print c.f
c.f = 2
print c.f
print C.f
