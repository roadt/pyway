
from pywebio.input import *

def check_age(p): # return None when the check passes, otherwise return the error message
    if p < 10:
        return "To young!!"
    if p > 60:
        return "Too old!!"

age = input("How old are you?", type=NUMBER, validate=check_age)
