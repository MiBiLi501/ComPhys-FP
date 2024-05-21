import pygame as pyg
import time

from Environment import Environment
from DynamicBody import DynamicBody
from Point import Point
from Spring import Spring

pyg.font.init()
# WINDOW_SIZE = 
screen = pyg.display.set_mode((1000, 600))

screen.fill((255, 255, 255))

clock = pyg.time.Clock()

coord = (100, 50)

env = Environment(1000, 600)

p1, p2, p3 = Point(pos=(200, 200)), Point(pos=(200, 400)), Point(pos=(300, 200))
body = DynamicBody(origin=(200, 200), points=[p1, p2, p3], springs=[Spring(obj1=p1, obj2=p2, s=1, l=100, d=0), Spring(obj1=p1, obj2=p3, s=1, l=100, d=0)])

env.add_dynamic_body(body)

cur = time.time()
prev = cur

running = True
while running:
    
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
    