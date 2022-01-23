#!/usr/bin/env python3

import mincepy
import uuid


#Creating types
class Person(mincepy.SimpleSavable):
    TYPE_ID = uuid.UUID('26798d9e-8c78-430a-ab2c-b17d612ef5fe')
    name = mincepy.field()
    age = mincepy.field()



#Storing objects
historian = mincepy.connect('mongodb://127.0.0.1/mince-quick-start', use_globally=True)

martin = Person(name='Martin', age=34)
martin_id = historian.save(martin)

# Let's save a couple more
sonia_id, upul_id = historian.save(
    Person(name='Sonia', age=30), Person(name='Upul', age=35))

# We can call .save() on the object as we have inherited from SimpleSavable
gavin = Person(name='Gavin', age=34)
gavin_id = gavin.save()

print(martin_id, sonia_id)



#Loading objects
del martin

martin, sonia = historian.load(martin_id, sonia_id)
print("{}, {}".format(martin.name, martin.age))   #        Martin, 34


#Finding objects
for person in historian.find(Person.age==34):
    print('{}, {}'.format(person.name, person.age))
Martin, 34
Gavin, 34


#Modifying objects
sonia.age = 31
sonia.save()

# Let's double check!
del sonia
sonia = historian.load(sonia_id)
print(sonia.age)   #   31


#Annotating objects
historian.meta.set(sonia, dict(city='Copenhagen'))
# Can also do it like this:
martin.set_meta(dict(city='Copenhagen'))
gavin.set_meta(dict(city='Glasgow'))
print(historian.meta.get(gavin))  #   {'city': 'Glasgow'}


#Searching metadata
for person in historian.find(Person.age==34, meta=dict(city='Glasgow')):
    print("{}, {}".format(person.name, person.age))
    Gavin, 34


#Version control
records = list(historian.snapshots.records.find(obj_id=sonia_id))
for record in records:
    print("{}, {}".format(record.version, record.state))

#0, {'name': 'Sonia', 'age': 30}
#1, {'name': 'Sonia', 'age': 31}






