
import time
from pywebio.input import *
from pywebio.output import *


i = 0 

def click():
    global i
    i+=1
    put_button(i, onclick=click)

click()

input('Stop')



