


import os, zipfile

print __file__

me = zipfile.ZipFile(os.path.dirname(__file__), 'r')
f = me.open('other.txt')
print f.read()
f.close()
me.close()


