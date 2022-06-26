

from collections import *


# Counter

########### deque #####################

# append/appendleft
dq = deque()
dq.append('1')
dq.appendleft('left')
print dq

# extend/extendleft
from copy import *
dq2 = copy(dq)
dq.extend([11,11])
print dq
dq.extendleft([12,12])
print dq

#count
print dq.count(11)

#remove
dq.remove(11)   #only remove a 11
print dq.count(11)
print dq

# pop/popleft
print dq.popleft()
print dq.pop()
print dq

# reverse
dq.reverse()
print 'reverse:\t', dq

# rotate
dq.rotate()
print 'rotate:\t', dq
dq.rotate()
print 'rotate:\t' , dq

# __reversed__
for n in dq:
    print n,
print

for n in reversed(dq):
    print n,
print

# __sizeof__
print '__sizeof__:',  len(dq)

# clear
dq.clear()
print dq






# defaultdict


# namedtuple

# OrderedDict
