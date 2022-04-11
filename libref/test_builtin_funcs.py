

#abs
abs(-10)
abs(-1.2)

#all()
#any()

#basestring()

#bin()
bin(22)

#bool()

#bytearray()

#callable()

#chr()

#classmethod()

#cmp()

#compile()

#complex()

#delattr()

#dict()

#dir()

#divmod()

#enumerate()

#eval()

#execfile()

#file()

#filter()


#float()

#format()

#frozenset()

#getattr()

#globals()

#hasattr()

#hash()

#help()

#hex()

#id()


#input()

#int()

#isinstance()

#issublcass()

#iter()

#len()

#list()

#locals()

#long()

#map()

#max()


#memoryview()

#min()

#next()

#object()

#oct()


#open()


#ord()

#pow()

#print()

#property() - class property([fget[, fset[, fdel[, doc]]]])

class C(object):
    def __init__(self):
        self._x = None
    
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
        
    x = property(getx, setx, delx, "I'm the 'x' property.")

c = C()
c.x
c.x = 3
c.x
del c.x


class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property    # only readonly/get
    def voltage(self):
        ''' Get the current voltage '''
        return self._voltage

p = Parrot()
p.voltage
# p.voltage = 100   #AttributeError: can't set attribute

class C2(object):
    def __init__(self):
        self._x = None
    
    @property
    def x(self):
        """ i'm the 'x' property. """
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
    
    @x.deleter
    def x(self):
        del self._x

c = C2()
c.x
c.x = 1000
c.x


#range(stop)
#range(start,stop[,step])



#raw_input()

#reduce()

#reload()

#repr()

#reversed()

#round()

#set()

#setattr()

#slice()

#sorted()


#staticmethod()

#str()

#sum()

#super()

#tuple()

#type()

#unichr()

#unicode()

#vars()

#xrange()

#zip()

#__import__()