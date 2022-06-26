#!/usr/bin/env python3

from ostruct import *

field = OpenStruct()

field.i = 1
field.s = "hello"
field.l = [1,2,3]
field.h = {'a':1, 'b':2}
field.h.a = 3

from pprint import pp

pp(field)



