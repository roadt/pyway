
import pywebio
from pywebio.input import *
from pywebio.output import *


def main():
    put_text('main')

#use_scope()
with use_scope('scope1'):  # open and enter a new output: 'scope1'
    put_text('text1 in scope1')  # output text to scope1

put_text('text in parent scope of scope1')  # output text to ROOT scope

with use_scope('scope1'):  # enter an existing scope: 'scope1'
    put_text('text2 in scope1')  # output text to scope1


#can use clear parameter in use_scope() to clear the existing content before entering the scope:
with use_scope('scope2'):
    put_text('create scope2')

put_text('text in parent scope of scope2')

with use_scope('scope2', clear=True):  # enter the existing scope and clear the previous content
    put_text('text in scope2')



#use_scope() can also be used as decorator:
from datetime import datetime

@use_scope('time', clear=True)
def show_time():
    put_text(datetime.now())


#Scopes can be nested. 
with use_scope('A'):
    put_text('Text in scope A')

    with use_scope('B'):
        put_text('Text in scope B')

with use_scope('C'):
    put_text('Text in scope C')


#
#put_scope()
#
put_table([
    ['Name', 'Hobbies'],
    ['Tom', put_scope('hobby', content=put_text('Coding'))]  # hobby is initialized to coding
])

with use_scope('hobby', clear=True):
    put_text('Movie')  # hobby is reset to Movie

# append Music, Drama to hobby
with use_scope('hobby'):
    put_text('Music')
    put_text('Drama')

# insert the Coding into the top of the hobby
put_markdown('**Coding**', scope='hobby', position=0)


#
#put_row() and put_column():
#
put_row([
    put_column([
        put_code('A'),
        put_row([
            put_code('B1'), None,  # None represents the space between the output
            put_code('B2'), None,
            put_code('B3'),
        ]),
        put_code('C'),
    ]), None,
    put_code('D'), None,
    put_code('E')
])
#put_row([put_image(...), put_image(...)], size='40% 60%')  # The ratio of the width of two images is 2:3

#
# Style
#
put_text('hello').style('color: red; font-size: 20px')

# in combined output
put_row([
    put_text('hello').style('color: red'),
    put_markdown('markdown')
]).style('margin-top: 20px')



