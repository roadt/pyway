

import pygame as p

# pygame.time
help(p.time)

# pygame.time.Clock
c = p.time.Clock()
help(c)
c.get_fps()
c.get_rawtime()
c.get_time()
c.tick()
c.tick_busy_loop()

# delay()
p.time.delay(1000)
p.time.get_ticks()

# set_timer()
help(p.time.set_timer)
p.time.set_timer(30, 1000)

# wait()
p.time.wait(1000)
