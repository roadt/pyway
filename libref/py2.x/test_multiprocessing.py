

from multiprocessing import *
from six import print_


# file:///usr/share/doc/python2/html/library/multiprocessing.html

# pool.map
def f(x):
    return x*x

p = Pool(5)
print_(p.map(f, [1,2,3]))


# Process
def f(name):
    print 'hello', name

p = Process(target=f, args=('bob',))
p.start()
p.join()




# 16.6.1.1 Process - class
# example to show parent pid
def info(title):
    print_(title)
    print_('module name:', __name__)
    
    if hasattr(os, 'getppid'): #only available on unix
        print_('parent process:', os.getppid())
    print_('process id:', os.getpid())

def f(name):
    info('function f')
    print_('hello', name)

info('main line')
p = Process(target=f, args=('bob',))
p.start()
p.join()


# 16.6.1.2  exchange object between processes

# Queues
def f(q):
    q.put([42, None, 'hello'])


q = Queue()
p = Process(target=f, args=(q,))
p.start()
print q.get()   # prints "[42, None, 'hello']"
p.join()



# Pipes
from multiprocessing import Process, Pipe

def f(conn):
        conn.send([42, None, 'hello'])
        conn.close()

parent_conn, child_conn = Pipe()
p = Process(target=f, args=(child_conn,))
p.start()
print parent_conn.recv()  # prints "[42, None, 'hello']"
p.join()



# 16.6.1.3  synchronized between process
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    print 'hello, world', i
    l.release()

lock = Lock()
for num in range(20):
    Process(target=f, args=(lock, num)).start()

# 16.6.1.4 sharing state between processes
# data can be stored in a shared memroy map using 'Value' or 'Array'
def f(n,a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

num = Value('d', 0.0)
arr = Array('i', range(10))
p = Process(target=f, args=(num, arr))
p.start()
p.join()

print_(num.value)
print_(arr[:])

# server process
def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

manager = Manager()
d = manager.dict()
l = manager.list(range(10))
p = Process(target=f, args=(d,l))
p.start()
p.join()

print d
print l


# 16.6.1.5 using a pool of workers
from multiprocessing import Pool

def f(x):
    return x*x

pool = Pool(processes = 4)
result = pool.apply_async(f, [10])
print result.get(timeout=1)            
print pool.map(f, range(10))                #print "[0,1,4,...,81]"


