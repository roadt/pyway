
from pywebio.input import *
code = textarea('Code Edit', code = {
    'mode': 'python',
    'theme': 'darcula'
}, value='import something\n#Write your python code here')


print(code)


code = textarea('Code Edit', code = {
    'mode': 'lua',
    'theme': 'darcula'
}, value='''
-- help 
function f() 
end
''')


print(code)
