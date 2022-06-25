#!/usr/bin/env python2

import pygame as p
import sys



class Game:
    def __init__(self):
        p.init()


class Scene:
    def __init__(self, scr, w, h):
        self.scr = scr
        self.u = min(self.scr.get_width()/w, self.scr.get_height()/h)
        self.w = w
        self.h = h

    def draw(self, x, y, c):
        if x < 0 or x > self.w:
            pass
        if y < 0 or y > self.h:
            pass
        p.draw.rect(self.scr, c, (self.u *x, self.u*y,  self.u, self.u))

    def bk(self, c):
        for  i in range(self.w+1):
            p.draw.line(self.scr, c, (i*self.u, 0), (i*self.u, self.h*self.u))
        for j in range(self.h+1):
            p.draw.line(self.scr, c, (0, j*self.u), (self.w*self.u, j*self.u))
            
    def clear(self, c):
        self.scr.fill(c)

    def pos(self, x, y):
        return (x/self.u, y/self.u)

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4    
class Snake:

    def __init__(self, x,y):
        self.blocks = [(x,y)]
        self.nblocks = 1
        self.dir = RIGHT
        self.speed = 1  # blk/s

    def add(self, x, y):
        self.blocks.insert(0, (x,y))
        self.nblocks = self.nblocks + 1
        
    def turn(self, d):
        ##  retriction on turn direction
        if self.dir in [UP, DOWN] and d in [LEFT, RIGHT]:
            self.dir = d
        if self.dir in [LEFT,RIGHT] and d in [UP,DOWN]:
            self.dir = d

    def draw(self, sc):
        for b in self.blocks:
            sc.draw(b[0], b[1], (255,0,0))

    def move(self):
        #for  i in reversed(range(1, self.nblocks)):
        #    self.blocks[i] = self.blocks[i-1]
        x,y = self.blocks[0]
        if self.dir == UP:
            y = y - 1
        elif self.dir == DOWN:
            y = y + 1
        elif self.dir == LEFT:
            x = x -1
        elif self.dir == RIGHT:
            x = x + 1
        self.blocks.pop()
        self.blocks.insert(0, (x,y))
                        
        
p.init()

clock = p.time.Clock()

size = width, height = 800, 600
speed = [10, 10]
black = 0, 0, 0
white = 255,255,255



screen = p.display.set_mode(size, p.HWSURFACE|p.DOUBLEBUF|p.RESIZABLE)
font = p.font.SysFont('sans', 16)

sn = Snake(0,0)
sn.add(0,1)
sn.add(1,1)
sn.add(1,2)
sn.add(2,2)

ball = p.image.load('ball.bmp')
ballrect = ball.get_rect()

mp = (0, 0)
while True:
    for evt in p.event.get():
        if evt.type == p.QUIT:
            p.quit()
            sys.exit()
        elif evt.type == p.MOUSEMOTION:
            mp = evt.pos
        else:
            print evt

    s = Scene(screen, 60, 60)
    s.clear(black)
    s.bk(white)

    pos = s.pos(*mp)
    s.draw(pos[0], pos[1], (0,0,255))
    sn.draw(s)
    p.display.flip()
    clock.tick(30)
