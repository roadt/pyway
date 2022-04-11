#!/usr/bin/env python2

from optparse import OptionParser

#
# step 1: a instance - parser = OptionParser()
# step 2: parser.add_option(opt_str,opt_long_str,  .., attr=value, ...)
# step 3: (optoins, args) = parser.parse_args()
#

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false",
                  dest="verbose",
                  default=True,
                  help="don't print status message to stdout")
# option attrs:  action, type, dest, help

(options, args) = parser.parse_args()
print (options, args)

#./test_optparse.py  -f adaf  -q asdfasfd asdf asdfasdf
# (<Values at 0x7ffa61feeab8: {'verbose': False, 'filename': 'adaf'}>, ['asdfasfd', 'asdf', 'asdfasdf'])