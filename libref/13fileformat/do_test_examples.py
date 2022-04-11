
import csv
from os.path import dirname, join

DIR=dirname(__file__)
fn = join(DIR, 'some.csv')


f = open(fn)
f.close()

with open(fn) as f:
    reader = csv.reader(fn)
    for row in reader:
        print(row)

