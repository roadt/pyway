
import pytest
import plyvel

db = plyvel.DB('/tmp/testdb/', create_if_missing=True)

def test_put():
    ''' put'''
    db.put(b'key', b'value')
    db.put(b'another-key', b'another-value')
    assert db.get(b'key') == b'value'

def test_get():
    '''get'''
    print(db.get(b'key'))
    print(db.get(b'yet-another-key'))

#delete
def test_delete():
    db.delete(b'key')
    db.delete(b'another-key')


#write-batch
wb = db.write_batch()
for i in range(100000):
    wb.put(str(i).encode(), str(i).encode() * 100)
wb.write()

for i in range(10):
    print(db.get(str(i).encode()))

#snapshot
db.put(b'key', b'first-value')

sn=db.snapshot()
sn.get(b'key')

db.put(b'key', b'second-value')
sn.get(b'key')

with db.snapshot() as sn:
    sn.get(b'key')

#iterators
for key, value in db:
    print(key)


for key, value in db.iterator(start=b'key-2', stop=b'key-4'):
    print(key)




#close
print(db.closed)
db.close()


