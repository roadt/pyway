
from pywebio.input import *
from pywebio.output import *


popup('Popup title', [
    put_html('<h3>Popup Content</h3>'),
    'plain html: <br/>',  # Equivalent to: put_text('plain html: <br/>')
    put_table([['A', 'B'], ['C', 'D']]),
    put_button('close_popup()', onclick=close_popup)
])


