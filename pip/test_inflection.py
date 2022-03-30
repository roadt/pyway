#!/usr/bin/env python

from inflection import *

s="gallery"
#camelize
camelize(s)
camelize(s+' '+s)
#dasherize
dasherize(s)
dasherize(s + ' ' +s)
#humanize
humanize(s)
humanize(s+' '+s)
#ordinal
#ordinalize
#parameterize
parameterize(u'Gallery')
parameterize(u'Galleries')
#pluralize
pluralize(s)
pluralize(s+' '+s)
#singularize
singularize(s)
singularize(s +' '+s)
#tableize
tableize(s)
tableize(s+ ' '+s)
#titleize
titleize(s)
titleize(s+ ' '+s)
#transliterate

#underscore
underscore(s)
underscore(s+' '+s)
#unicodedata