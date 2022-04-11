#!/usr/bin/env python2

import os

print os.path.join("a", "b", "c")


print os.makedirs('a/b')     # mode = 777
print os.makedirs('a/c', mode=0775)  

print os.removedirs('a/b')
print os.removedirs('a/c')


print os.renames('a/b', 'a/d')    # exists


#os.name   
# => posix, nt, os2, ce, riscos
os.name


# os.path
# os.path.curdir
os.path.curdir

# os.path.pardir
os.path.pardir

# os.path.sep
os.path.sep

# os.path.pathsep
os.path.pathsep

# os.path.defpath
os.path.defpath

# os.path.extsep
os.path.extsep

# os.path.altsep
os.path.altsep

# os.path.devnull
os.path.devnull


# os.makedirs
os.makedirs('a/b/c', mode=0777)

# os.walk
for root,dirs, files in os.walk('/home/roadt/tmp'):
    print [root, dirs, files]


# os.renames(old,new)
os.renames('a', 'a2')

# os.removedirs
os.removedirs('a/b/c')

# os.getenv(key,default=None)
os.getenv('HOME', 'xxx')

# execl, execle, execlp, execlpe, execvp, execvpe
os.execl('/home/roadt/.emacs', '')

