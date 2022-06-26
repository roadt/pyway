
import dataset

db = dataset.connect('sqlite:///:memory:')

t = db['t']
t.insert(dict(name='Name', age = 37))
t.insert(dict(name='xxx', age=2, gender='female'))

john = t.find_one(name='Name')
john