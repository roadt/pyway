#!/usr/bin/env python2


def fib(n):
	if n < 0:
		n = - n

	if fib.vals.has_key(n):
		return fib.vals[n]
	else:
		res =  fib(n-1) + fib(n-2)
		fib.vals[n] = res
	return res

fib.vals  = {0:1, 1:1, 2:2}


def fact(n):
	if n < 0:
		n  = -n

	if n == 0:
		return 1
	return n * fact(n-1)

print fact(400)
