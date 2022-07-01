#!/usr/bin/env python2



import pygame as p
import sys,os

os.chdir(os.path.dirname(__file__))

# init pygame modules (including display)
p.init()

size = w , h = 320, 240
speed = [2,2]
black = 0, 0 , 0

# get dispaly/set mode
s = p.display.set_mode(size)

ball = p.image.load('ball.bmp')
ballrect = ball.get_rect()

while 1:
    # retrive event
    for e in p.event.get():
        if e.type == p.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > w:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > h:
        speed[1] = -  speed[1]

    s.fill(black)
    s.blit(ball, ballrect)

    # flip display
    p.display.flip()

    



