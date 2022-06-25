#!/usr/bin/env python2

import pygame as p
import sys

p.init()

clock = p.time.Clock()

size = width, height = 800, 600
speed = [10, 10]
black = 0, 0, 0
white = 255,255,255



screen = p.display.set_mode(size, p.HWSURFACE|p.DOUBLEBUF|p.RESIZABLE)
font = p.font.SysFont('sans', 16)

ball = p.image.load('ball.bmp')
ballrect = ball.get_rect()

while True:
    for evt in p.event.get():
        if evt.type == p.QUIT:
            p.quit()
            sys.exit()
        else:
            print evt
    fps =  clock.get_fps()
    if fps >0:
        speed2 = [n*60/clock.get_fps() for n in speed]
    else:
        speed2 = speed
    ballrect = ballrect.move(speed2)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    s2 = font.render(str(clock.get_fps()), True, white)
    screen.blit(s2, (0,0))
                
    p.display.flip()
    clock.tick(1000000)
