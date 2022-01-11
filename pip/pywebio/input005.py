

from pywebio.input import *
from pywebio.output import *

def check_age(p): # return None when the check passes, otherwise return the error message
    if p < 10:
        return "To young!!"
    if p > 60:
        return "Too old!!"

def check_form(data):  # return (input name, error msg) when validation fail
    if len(data['name']) > 6:
        return ('name', 'Name too long!')
    if data['age'] <= 0:
        return ('age', 'Age can not be negative!')

#Input Group
data = input_group('Basic info', [
    input('Input your name', name='name'),
    input('Input your age', name='age', type=NUMBER, validate=check_age)
    ], validate=check_form)
put_text(data['name'], data['age'])

