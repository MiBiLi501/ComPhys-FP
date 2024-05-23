import pygame as pyg
import time

from Environment import Environment
from DynamicBody import *

pyg.font.init()
# WINDOW_SIZE = 
screen = pyg.display.set_mode((1000, 600))

pyg.display.set_caption("Soft Body simulation")

screen.fill((255, 255, 255))

clock = pyg.time.Clock()

coord = (100, 50)

env = Environment(1000, 600)

p1, p2, p3 = Point(pos=(200, 200)), Point(pos=(200, 400)), Point(pos=(300, 200))
body = SpringMassBody(origin=(200, 200), points=[p1, p2, p3], springs=[Spring(obj1=p1, obj2=p2, s=1, l=100, d=0.5), Spring(obj1=p1, obj2=p3, s=1, l=100, d=0.1), Spring(obj1=p2, obj2=p3, s=1, l=100, d=0.1)])

p4, p5, p6 = Point(pos=(600, 200)), Point(pos=(270, 600)), Point(pos=(600, 500))
body2 = SpringMassBody(origin=(200, 200), points=[p4, p5, p6], springs=[Spring(obj1=p5, obj2=p6, s=1, l=100, d=0.1), Spring(obj1=p4, obj2=p6, s=1, l=100, d=0.1)])

env.add_dynamic_body(body)
env.add_dynamic_body(body2)

# p1, p2 = Point(pos=(200, 200)), Point(pos=(200, 400))
# body = SpringMassBody(origin=(200, 200), points=[p1, p2, ], springs=[Spring(obj1=p1, obj2=p2, s=1, l=100, d=0)])
# env.add_dynamic_body(body)

cur = time.time()
prev = cur

running = True
while running:
    # input()
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    while(cur-prev < 1/60): cur = time.time()

    # Rendering
    screen.fill((255, 255, 255))
    
    env.update()

    env.draw(screen)

    pyg.display.flip()

    # Update environment
    