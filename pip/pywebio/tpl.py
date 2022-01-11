
import pywebio
from pywebio.input import *
from pywebio.output import *


def main():
    put_text('main')


if __name__ == '__main__':
    pywebio.start_server(main, port=8000) 
