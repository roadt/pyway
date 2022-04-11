#!/usr/bin/env python2

import chardet
import sys


def txt2buf(p):
    with file(p) as f:
        return f.read()



if __name__ == '__main__':
	argv = sys.argv
	argc = len(argv)
	if argc < 2:
		print '%s <file>' % (argv[0])
		sys.exit(1);

    print chardet.detect(txt2buf(argv[1]));
		
