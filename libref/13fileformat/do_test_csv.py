

import csv
from os.path import dirname, join

DIR=dirname(__file__)
CSVPATH = join(DIR, 'some.csv')


print( csv.list_dialects())

# sniffer use
# with open('example.csv', 'rb') as csvfile:
#     dialect = csv.Sniffer().sniff(csvfile.read(1024))
#     csvfile.seek(0)
#     reader = csv.reader(csvfile, dialect)
    # ... process CSV file contents here ...


# csv.reader(csvile, dialect='excel', **fmtparams)
import csv
with open('/etc/passwd', 'rb') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    print( reader.fieldnames)
    for row in reader:
        print (row)


# csv.writer(csvfile, dialect='excel', **fmtparams)


# csv.register_dialect(name, [dialect,]**fmtparams)


# csv.unregister_dialect(name)

# csv.get_dialect(name)

# csv.list_dialects()

# csv.field_size_limit([new_limit])



# csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
import csv
with open(CSVPATH) as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    for row in reader:
        print(row['name'], row['url'])

def get_csv_objects(fn):
    with open(fn) as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        ret = []
        for row in reader:
            ret.append(row)
        return headers, ret

l = get_csv_objects('names.csv');print(l)

# csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'first_name':'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name':'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name':'Wonderful', 'last_name': 'Spam'})

def write_csv_objects(fn, header_data_tuple):
    with open(fn, 'w') as csvfile:
        headers, data = header_data_tuple
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


write_csv_objects('names.csv', (['a', 'b'], [{'a':1,'b':2}, {'a':3,'b':4}]))
        

# csv.Dialect

# csv.excel

# csv.excel_tab

# csv.Sniffer


# csv.QUOTE_ALL

# csv.QUOTE_MINIMAL 

# csv.QUOTE_NONNUMRIC

# csv.QUOTE_NONE



