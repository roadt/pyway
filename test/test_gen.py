

# test generator


def f(n):
    for n in range(n):
        i = yield n 
        print i*i

g = f(10)

g.send(None)

# the number will send to generator execution, and print by "print i*i"
g.send(16)
g.send(256)
