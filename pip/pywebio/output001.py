
from pywebio.input import *
from pywebio.output import *

put_text("Hello, world!")


put_table([
    ['Commodity', 'Price'],
    ['Apple', '5.5'],
    ['Banana', '7'],
])

put_image(open('/RAD/studies/comp/lang/python/lib/pywebio/icon50.png', 'rb').read())
put_image('https://img.icons8.com/bubbles/344/flying-duck.png')


put_markdown('~~Striekthrough~~')

put_file('hello_world.txt', b'hello world!')

popup('popup title', 'popup text content')

toast('New message 🔔')

