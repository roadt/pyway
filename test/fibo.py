#!/usr/bin/env python


def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)

def fib1(n):
    for i in range(100):
        print i, '-', fib(i)

def fib2(n):
    a,b = 0, 1
    for i in range(n):
        c = b
        b = a+ b
        a = c
        print i, '-', b
    

