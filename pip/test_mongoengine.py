

from mongoengine import *
connect('test')



class  A(Document):
    a = StringField()

print(dir(A))


