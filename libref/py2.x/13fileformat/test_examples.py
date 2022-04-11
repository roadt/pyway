
import csv



fn = '/RAD/studies/comp/lang/python/libref/13fileformat/some.csv'

f = open(fn)
f.close()

reader = csv.reader(f)
with open(fn) as f:
    reader = csv.reader(f)
    for row in reader:
        print row
