#!/usr/bin/env python2



import pygame as p
import sys,os

os.chdir('/RAD/studies/comp/lang/python/lib/pygame/')

# init pygame modules (including display)
p.init()

size = w , h = 320, 240
black = 0, 0 , 0

# get dispaly/set mode
s = p.display.set_mode(size)



while 1:
    # retrive event
    for e in p.event.get():
        if e.type == p.QUIT: sys.exit()

    # logic code

    # draw code
    s.fill(black)
    #s.blt(image, rect)

    # flip display
    p.display.flip()

    
