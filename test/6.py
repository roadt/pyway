#!/usr/bin/env python2

#
#  test for special method
#
#

class C:
	def __init__(self):
		self.a = 1
		self.b = 2

	def __getattr__(self, k):
		print  'get_' + k
		return str


c1 = C()

print c1
print c1[1]
