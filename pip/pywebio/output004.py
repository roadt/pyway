
from pywebio.input import *
from pywebio.output import *

with put_collapse('This is title'):
    for i in range(4):
        put_text(i)

    put_table([
        ['Commodity', 'Price'],
        ['Apple', '5.5'],
        ['Banana', '7'],
    ])
