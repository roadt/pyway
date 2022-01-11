from pywebio import start_server
from pywebio.input import *
from pywebio.output import *

#Click Callback
from functools import partial

def edit_row(choice, row):
    put_text("You click %s button ar row %s" % (choice, row))

put_table([
    ['Idx', 'Actions'],
    [1, put_buttons(['edit', 'delete'], onclick=partial(edit_row, row=1))],
    [2, put_buttons(['edit', 'delete'], onclick=partial(edit_row, row=2))],
    [3, put_buttons(['edit', 'delete'], onclick=partial(edit_row, row=3))],
])



# also supports outputting individual button:
def btn_click(btn_val):
    put_text("You click %s button" % btn_val)

put_buttons(['A', 'B', 'C'], onclick=btn_click)  # a group of buttons

put_button("Click me", onclick=lambda: toast("Clicked"))  # single button


# can call onclick() method after the output function (function name like put_xxx()) call:
put_image('some-image.png').onclick(lambda: toast('You click an image'))  
# set onclick in combined output
put_table([
    ['Commodity', 'Price'],
    ['Apple', put_text('5.5').onclick(lambda: toast('You click the text'))],
])


#
input()
