#!/usr/bin/env python2

# test fucntion argument passing  
# and the immutable (string, number).


def f1(s):
	s[0] = 'c'
	return s

a = 'hello,world'
f1(a)

