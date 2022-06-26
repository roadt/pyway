#!/usr/bin/env python3

import logging
import time

from timer import timer

# timer would print nothing without this line or logging level is info or higher
logging.basicConfig(level=logging.DEBUG)


# explicit the timer's name and it's time unit
@timer('function:add', unit='s')
def add(a, b):
    time.sleep(.1)
    return a + b


# function name is timer's name for default
@timer
def sub(a, b):
    time.sleep(.1)
    return a - b


if __name__ == '__main__':
    # 'timer' would be timer's name by default
    with timer('time.sleep(2)') as t:
        print(3)
        time.sleep(1)
        print(f'after time.sleep(1) once, t.elapse = {t.elapse}')
        time.sleep(1)
        print(f'after time.sleep(1) twice, t.elapse = {t.elapse}')
    print(f'after with, t.elapse = {t.elapse}')

    print(add(1, 1))
    print(sub(2, 1))
