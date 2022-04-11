#!/usr/bin/env python
#
#
#
class File(object):
    def __init__(self, file, fh):
        self.file = file
        self.fh = fh
        self.pos = fh.tell()

    def __getstate__(self):
        return { 'file': self.file, 'pos':self.pos}

    def __setstate__(self, dict):
        self.file = dict['file']
        self.pos = dict['pos']
        self.fh = open(self.file)
        self.fh.seek(self.pos)
        
    def readline(self):
        s = self.fh.readline()
        self.pos = self.fh.tell()
        return s


#
# a text reader  which support persistence.
#
class TextReader:
    """ print and number lines in a text file. """
    def __init__(self, file):
        self.file = file
        self.fh = open(file)
        self.lineno = 0

    def readline(self):
        self.lineno = self.lineno + 1
        line = self.fh.readline()
        if not line:
            return None
        if line.endswith("\n"):
            line = line[:-1]
        return "%d: %s" %(self.lineno, line)

    def __getstate__(self):
        odict = self.__dict__.copy()
        del odict['fh']
        return odict

    def __setstate__(self, dict):
        fh = open(dict['file'])
        self.__dict__.update(dict)
        self.fh = fh
        count = dict['lineno']
        while count:
            fh.readline()
            count = count - 1



class TextReader2:
    """ print and number lines in a text file. """
    def __init__(self, file):
        self.file = File(file, open(file))
        self.lineno = 0

    def readline(self):
        self.lineno = self.lineno + 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith("\n"):
            line = line[:-1]
        return "%d: %s" %(self.lineno, line)


import pickle

        
#
# test 
# 

def test_do_and_stop():
    obj = TextReader2("test_TextReader.py")
    for n in range(10):
        print obj.readline();
    pickle.dump(obj, open("test_TextReader.sav", "wb"))
    print '-----------stop ---------'
    print obj.file, obj.lineno
    del obj

def test_restore_and_continue():
    reader = pickle.load(open("test_TextReader.sav", "rb"))
    print '---- now, recoverd , continue -------'

    for n in range(10):
        print reader.readline()


def test():
    test_do_and_stop()
    test_restore_and_continue()



#
# startup code
#
if __name__ == "__main__":
    test()
