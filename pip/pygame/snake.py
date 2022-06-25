#!/usr/bin/env python2

import pygame as p
import sys

size = w, h = 800, 600
black = 0, 0, 0
white = 255,255,255
blue = 0,0,255

class scene:
    def __init__(self, scr, w, h, u):
        self.w = w / u
        self.h = h / u
        self.u = u
        self.scr = scr

    def drawbk(self):
        for  i in range(self.w+1):
            p.draw.line(scr, white, (i*self.u, 0), (i*self.u, self.h*self.u))
        for j in range(self.h+1):
            p.draw.line(scr, white, (0, j*self.u), (self.w*self.u, j*self.u))

    def drawblk(self, x,y):
        if x < 0 or x > self.w:
            pass
        if y < 0 or y > self.h:
            pass
        p.draw.rect(self.scr, blue, (self.u *x, self.u*y,  self.u, self.u))


UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

class snake:
    def __init__(self, sc, x,y):
        self.sc = sc
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

    def draw(self):
        for b in self.blocks:
            self.sc.drawblk(*b)

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
scr = p.display.set_mode(size, p.HWSURFACE|p.DOUBLEBUF)
font = p.font.SysFont('Tahoma,Sans', 12)


def text(s, x, y):
    s = font.render(s, True, white)
    scr.blit(s, (x,y))


s = scene(scr, w, h, 16)
sk = snake(s, 0, 0)
for i in range(20):
    sk.add(0, i)

while True:
    for evt in p.event.get():
        if evt.type == p.QUIT:     
            p.quit()
            sys.exit()
        elif evt.type == p.KEYDOWN:
            scancode = evt.dict['scancode']
            key = evt.key
            if key == p.K_UP:
                sk.turn(UP)
            elif key == p.K_LEFT:
                sk.turn(LEFT)
            elif key == p.K_RIGHT:
                sk.turn(RIGHT)
            elif key == p.K_DOWN:
                sk.turn(DOWN)
        else:   
            print evt
    scr.fill(black)
    #s.drawbk()
    sk.move()
    sk.draw()
    text('msg', 1, 1)
    
    p.display.flip()
    clock.tick(1)

            
        
        
    
