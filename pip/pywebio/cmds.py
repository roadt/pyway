
import pywebio
from pywebio.input import *
from pywebio.output import *



def home():
    put_text('Home!')

def ok():
    toast('ok')

def square():
    s = input('num', type=NUMBER)
    put_text("%s*%s=%s"% (s,s,s*s))

funcs = [home, ok, square]
def main():
    for f in funcs:
        put_button(f.__name__, onclick=f)


if __name__ == '__main__':
    pywebio.start_server(main, port=8000) 
