#!/usr/bin/env python2

# file:///usr/share/doc/python2/html/library/stdtypes.html


import unittest
# file.close
class FileTypeTestCase(unittest.TestCase):
    def test_close(self):
        f = file('tmp')
        f.close()

# file.flush


# file.fileno


# file.isatty

# file.next

# file.read([size])

# file.readline([size])

# file.readlines([sizehint])


# file.seek(offset[, where])

# file.tell()


# file.truncate([size])

# file.write(str)

# file.writelines(sequence)

# file.closed


# file.encoding


# file.errors

# file.mode

# file.name

# file.newlines

# file.softspace



try:
    unittest.main()
except e, Error:
    print e

